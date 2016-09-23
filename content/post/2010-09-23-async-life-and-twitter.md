---
title: Async life and twitter
author: koblas
layout: post
date: 2010-09-23T15:54:33+00:00
url: /p/async-life-and-twitter/311
pvc_views:
  - 6866
aktt_tweeted:
  - 1
aktt_notify_twitter:
  - yes
dsq_thread_id:
  - 160932671
categories:
  - Development
tags:
  - amqp
  - python
  - tornado
  - twisted

---
The project of the week, is something that I&#8217;ve been putting off for a **very** long time.  Which is to get something running on [Extra][1] that&#8217;s more than just a nothing site.  Part of the problem is that it&#8217;s a good domain name that I&#8217;ve had parked for a very long time, and it makes real $$ in parking revenue, which I would rather not endanger.

FYI &#8212; The real purpose of this post is to document the code fragment at the bottom&#8230;  Though for those other readers, take a look at how I&#8217;ve played around with some attributes of [twitter feeds on extra.com][2] [discussion threading and tagging].

One of the many ideas that I&#8217;ve had is to basically build a celeb following website, well after last week and building [Notewave][3] as a demonstration that it is possible to build an async chat style site.  My thoughts got bigger, so here&#8217;s what I needed:

  * Tornado for the async webserver, already build the [django to tornado][4] connector previously.
  * Twitter stream reader, which I have a few laying around.  Though they&#8217;re all built with the twisted framework, but while I&#8217;ve got a bunch wan&#8217;t to get out of the NIH habit so ended up using this [twitter+twisted][5] on github.
  * We&#8217;ll skip over all of the OAuth pain for some other twitter usages.

The original implementation had one process reading the twitter stream and then doing an HTTP post to the webserver to notify it that it had received a post from twitter.  This was nice, but I was now getting reports of 700K web requests, which was making my logs big and the ability to figure out if anybody was using the service just about impossible (ok, yes Google Analytics is there).  So, this mornings 5am project was to get AMQP back into the running.

I&#8217;ve used AMQP before &#8212; wrote a full scale web crawler that had a few components that utilized AMQP as the message system (it was actually AMQP + Thrift).  It worked and message passing systems are really very sweet to work with.  The challenge in this is that I had two different async frameworks (Twisted and Tornado) that I needed to get AMQP integrated with.

The Twisted one was pretty easy &#8212; there&#8217;s txAMQP which is &#8220;ok&#8221;, I&#8217;ve got a wrapper around it from my webcrawler that actually makes it easy to use.  The Tornado one was a bit more difficult, the challenge was that there is an AMQP + async python implementation, but it didn&#8217;t support Tornado as the server.  So, off to dig around through mailing lists, and other sources..

Finally found what I wanted with was [AMPQ+Tornado+Pika][6] as a unofficial port&#8230;  This worked great, except the documentation is so lacking!  Which really brings us to the point of this posting&#8230;  The quick integration for this project.

```python
# Tornado listener
from pika.tornado_adapter import TornadoConnection
import pika
import json

class Handler(object) :
    def __init__(self, amqp=None, channel=None) :
        self.amqp = amqp
        self.channel = channel

    def startup(self) :
        channel = self.amqp.channel()
        channel.queue_declare(queue='extra_ui', durable=False, exclusive=False, auto_delete=True)
        channel.queue_bind(queue='extra_ui', exchange='celeb.tweet_ids')

        channel.basic_consume(self.recv, 'extra_ui')

    def recv(self, channel, method, header, body) :
        v = json.loads(body)

        from views.chat import post_notify
        post_notify(v['id'])

        channel.basic_ack(delivery_tag=method.delivery_tag)

def init() :
    handler = Handler()

    amqp = TornadoConnection(pika.ConnectionParameters('localhost',
    heartbeat = 10,
    credentials = pika.PlainCredentials('guest', 'guest')),
    callback=handler.startup)

    handler.amqp = amqp
```

Doing my quick blogpost code review, says that I could have done things much better&#8230;  Moved the ConnectionEstablishment into the Handler class, etc, etc.  But at the time I was more interested in getting things working at now 6:30am&#8230;  The big things I found was that the queue bits needed to be in the callback after the connection was established, otherwise RabbitMQ dropped things on the floor for out of order reasons.

 [1]: http://www.extra.com
 [2]: http://celeb.snaplabs.com/joshwolfcomedy
 [3]: http://notewave.com
 [4]: http://github.com/koblas/django-on-tornado
 [5]: http://github.com/fiorix/twisted-twitter-stream
 [6]: http://github.com/gmr/pika
