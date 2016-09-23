---
title: ioloop as a core concept
author: koblas
layout: post
date: 2013-02-10T04:58:02+00:00
url: /p/ioloop-as-a-core-concept/505
pvc_views:
  - 5977
dsq_thread_id:
  - 1074798209
categories:
  - Development
tags:
  - fizzbuzz

---
In the begininning there was main() and that was good.  But under the surface that has changed, it&#8217;s still main() but what really happens is dynamic linking, exit handling resources&#8230;  We&#8217;re even throwing garbage collection in for good luck.  But, it&#8217;s still main().

Why?

If you do anything that&#8217;s isn&#8217;t linear programming you see that ioloop() is really main and you have boilerplate to set up everything for your call to the ioloop().  So, now main isn&#8217;t really important we&#8217;re boiler plating main() into a bunch of work for ioloop()&#8230;  But, alas the languages don&#8217;t support this, sometimes you can do things like

```python
@gen.engine
def fizzle(self):
    result = yield gen.Task(some_function, args)
```

Why should I do all that &#8211; if the language assumed all IO operations needed to yield to ioloop() the syntax would support that model. You wouldn&#8217;t need to worry about what was sync and async, you wouldn&#8217;t need to wrap and decorate.  It would just be good.

Imagine- open(), read(), write() socket(), connect() all assumed they were async and would default yield to the ioloop&#8230;

Now to write this language&#8230;  Maybe I&#8217;ll call it &#8220;eve&#8221;, but the $64k question is compiled or interpreted&#8230;

**Update:** This really is the &#8220;async&#8221; that is proposed for Python 3.5 &#8211; hope it makes it.
