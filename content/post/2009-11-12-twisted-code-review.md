---
title: Twisted code review…
author: koblas
layout: post
date: 2009-11-12T17:04:11+00:00
url: /p/twisted-code-review/261
aktt_tweeted:
  - 1
pvc_views:
  - 6540
dsq_thread_id:
  - 160532041
categories:
  - Development
tags:
  - python
  - thrift
  - twisted

---
If you have a few minutes and speak python & twisted, it would be useful to have an extra set of eyes on this section of code. The basic idea of this is to be a reconnecting thrift client, such that I can just write simple client.function(a,b,c) calls without having to worry about if there is or isn&#8217;t a client and it will queue reconnect as needed.

```python
from thrift.transport import TTwisted
from thrift.protocol import TBinaryProtocol
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import defer, reactor
from twisted.python import failure
from collections import deque
from redback import log

class ClientBusy(Exception):
    pass

class ClientDead(Exception):
    pass

class InvalidThriftRequest(Exception):
    pass

class ManagedThriftRequest(object):
    def __init__(self, method, *args, **kw) :
        self.method = method
        self.args = args
        self.kw = kw

class ManagedClient(object) :
    def __init__(self, factory) :
        self.__factory = factory

    def _is_connected(self) :
        return self.__factory.is_connected()

    def __getattr__(self, name) :
        if hasattr(self.__factory.client_class, name) :
            def f(*args, **kw) :
                return self.__factory.pushRequest(ManagedThriftRequest(name, *args, **kw))
                return f
        raise InvalidThriftRequest("Cant find method: %s" % name)

class ManagedThriftClientProtocol(TTwisted.ThriftClientProtocol):
      
    def __init__(self, client_class, iprot_factory, oprot_factory=None):
        TTwisted.ThriftClientProtocol.__init__(self, client_class, iprot_factory, oprot_factory)
        self.client_class = client_class
        self.deferred = None
        self.alive = False

    def connectionMade(self):
        log.debug(self, "Connection made to", "%s.%s" % (self.client_class.__module__, self.client_class.__name__), "[%s]:%s" % self.transport.addr)
        self.alive = True
        TTwisted.ThriftClientProtocol.connectionMade(self)
        self.client.protocol = self
        self.factory.clientIdle(self)

    def connectionLost(self, reason=None):
        log.debug(self, "Connection lost to", "%s.%s" % (self.client_class.__module__, self.client_class.__name__), "[%s]:%s" % self.transport.addr)
        self.alive = False
          
        try :
            TTwisted.ThriftClientProtocol.connectionLost(self, reason)
            self.factory.clientGone(self)
        except Exception, e :
            log.error(self.connectionLost, e)

    def _complete(self, res, request, dfd):
        self.deferred = None
        if isinstance(res, failure.Failure) and dfd :
            self.factory.pushRequest(request, dfd)
        else :
            if dfd :
                dfd.callback(res)
            self.factory.clientIdle(self)
        return res

    def submitRequest(self, request, dfd):
        if not self.alive :
            raise ClientBusy
        if not self.deferred :
            fun = getattr(self.client, request.method, None)
            if not fun:
                raise InvalidThriftRequest("No such method as : %s" % request.method)
            else :
                try :
                    d = fun(*request.args, **request.kw)
                except Exception, e :
                    log.error(self.submitRequest, "calling : ", request.method, e)
                self.deferred = d
            d.addBoth(self._complete, request, dfd)
            return d
        else:
            raise ClientBusy

class ManagedClientFactory(ReconnectingClientFactory):
    maxDelay = 5
    thriftFactory = TBinaryProtocol.TBinaryProtocolAcceleratedFactory
    protocol = ManagedThriftClientProtocol
    submitLoopSleep = 0
    client_class = None

    def __init__(self, client_class=None):
        self._stack = deque()
        self._protos = defer.DeferredQueue()
        self.deferred = defer.Deferred()
        self.client_class = client_class or self.client_class
        self.client = ManagedClient(self)

    def _errback(self, reason=None):
        if self.deferred :
            self.deferred.errback(reason)
        self.deferred = None

    def _callback(self, value=None):
        if self.deferred :
            self.deferred.callback(value)
        self.deferred = None

    def clientConnectionFailed(self, connector, reason):
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)
        self._errback(reason)

    def buildProtocol(self, addr) :
        self.resetDelay()
        p = self.protocol(self.client_class, self.thriftFactory())
        p.factory = self
        #self._protos.put(p)
        return p

    def clientIdle(self, proto) :
        self._callback(True)
        if proto.alive :
            self._protos.put(proto)

    def clientGone(self, proto):
        pass
        #if proto in self._protos :
        # self._protos.remove(proto)

    def _protoErr(self, proto):
        pass
        #import traceback
        #traceback.print_stack()
        #print "IN PROTO ERR", proto

    def _protoReady(self, proto):
        if proto.deferred :
            log.msg(self._protoReady, "Proto currently active!")
            return
          
        if not proto.alive :
            log.msg(self._protoReady, "Proto currently dead!")
            return
        try:
            request, deferred = self._stack.popleft()
        except defer.QueueUnderflow :
            pass
        d = proto.submitRequest(request, deferred)
        return d

    def pushRequest(self, request, din=None) :
        d = din or defer.Deferred()
        self._stack.append((request, d))
        dfd = self._protos.get()
        dfd.addCallback(self._protoReady)
        dfd.addErrback(self._protoErr)
        return d

    def shutdown(self) :
        """Shutdown this factory"""
        self.stopTrying()
        for p in self._protos:
            if p.transport:
                p.transport.loseConnection()

```
