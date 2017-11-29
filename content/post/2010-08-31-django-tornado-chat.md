---
title: Django + Tornado = Chat
author: koblas
type: post
date: 2010-08-31T20:37:47+00:00
url: /p/django-tornado-chat/305
pvc_views:
  - 17568
aktt_tweeted:
  - 1
dsq_thread_id:
  - 160711093
categories:
  - Development
tags:
  - python
  - django

---
Just finished up a quick one day project&#8230;  Was curious about Torando and since I&#8217;ve been playing with Django wondered about mixing the two&#8230;   Of course at one level there isn&#8217;t much reason to put django and tornado together since django has a &#8220;fine&#8221; webserver built in and Torando is all about async.

Thus you need to invent an app that requires async, traditional http chat with long polling is the trick.  So, pulling a demo from the NodeJS land and building a bunch of glue work I ended up with a working Django+Torando = Chat application.  Sorry there is no demo, since it looks and works pretty much like the NodeJS chat application (borrowed their UI and JS).

However if you want to check out the code take a look at this:

<http://github.com/koblas/django-on-tornado>

The key part that&#8217;s interesting is this ability to add asyn requests to a django handler:

```python
from django_tornado.decorator import asynchronous

@asynchronous
def recv(request, handler):
    response = {}

    if 'since' not in request.GET :
        return ChatResponseError('Must supply since parameter')
    if 'id' not in request.GET :
        return ChatResponseError('Must supply id parameter')

    id = request.GET['id']
    session = Session.get(id)
    if session :
        session.poke()

    since = int(request.GET['since'])

def on_new_messages(messages) :
    if handler.request.connection.stream.closed():
        return
    handler.finish({ 'messages': messages, 'rss' : channel.size() })

    channel.query(handler.async_callback(on_new_messages), since)</pre>
```
