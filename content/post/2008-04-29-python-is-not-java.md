---
title: Python is not Java
author: koblas
layout: post
date: 2008-04-29T20:01:20+00:00
url: /p/python-is-not-java/145
pvc_views:
  - 5253
dsq_thread_id:
  - 160531883
categories:
  - General

---
I admit it, I&#8217;ve been working on my middleware python server.&nbsp;&nbsp; Here&#8217;s the basic design of the app at this point:

> PHP <&#8212; JSON-RPC &#8212;-> Python <&#8211;> MySql

The assumption is that as things grow, you&#8217;ve already defined a good layer to scale at and have a reasonable Object abstraction from the front end.&nbsp; At one level it&#8217;s turning out to be duplication of work, like duh!&nbsp; I almost need three versions of the same object instance.

  1. the ORM version (read/write to the DB) 
  2. the Python version &#8212; manipulation and management 
  3. the PHP version &#8212; slightly different mix of methods, but same data

That&#8217;s the object trials and tribulations.&nbsp; Now we&#8217;re off to RPC land.&nbsp; First you have to pick a framework, which if you want to use Python and JSON-RPC [lighter weight than XML-RPC] you end up in a world of hurt since the jsonrpc support for the long laundry list of frameworks is pretty piss poor.&nbsp; 

Currently using Twisted as the framework de jour, but it&#8217;s json-rpc library (via a code.google.com project) doesn&#8217;t quite match the spec!&nbsp; For instance by default it always returns a list.&nbsp; Second problem, which turns out to be a fun rant&#8230;&nbsp; This is where one really discovers that Python is not Java, is that if you want to serialize anything out via the Twisted mess of frameworks you&#8217;re waiting for pain.

  1. simplejson (as used by Twisted JSON-RPC) is slow 
  2. cjson is fast, but suffers even more than simplejson

Biggest problem, I want to have this nice simple return statement in my json handler:

```python
return { 'data': object }
```

Looks nice, but wait!&nbsp; simplejson doesn&#8217;t know what to do with an object.&nbsp; The only &#8220;fix&#8221; is to subclass simplejson to extend the handlers.&nbsp; Of course since I&#8217;m sitting eight layers down in the stack from where simplejson is instantiated you can&#8217;t really do that.&nbsp; So, what&#8217;s the fix?

**The Fix:** tear apart the Twisted JSON-RPC handler make it use both simplejson and cjson (why not) and add 4 lines of code to cjson encode_object:

```c
if ((result = PyObject_CallMethod(object, "__getstate__", NULL)) != NULL) {
    PyObject *r = encode_object(result);
    Py_XDECREF(result);
    return r;
}
```

Ah, now we&#8217;ve duck typed the pickle \_\_getstate\_\_ method to give us a back a dictionary&#8230;&nbsp; The problem of course is that you can&#8217;t register &#8220;unknown&#8221; type handlers for any of the json serializes out there.
