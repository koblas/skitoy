---
title: Python import improvements
author: koblas
layout: post
date: 2008-08-04T16:50:55+00:00
url: /p/python-import-improvements/175
pvc_views:
  - 5881
dsq_thread_id:
  - 163814042
categories:
  - General

---
[originally posted to comp.lang.python &#8212; but worth repeating]

Ruby has been getting pummeled for the last year or more on the performance subject. They&#8217;ve been working hard at improving it. From my arm chair perspective Python is sitting on it&#8217;s laurels and not taking this as seriously as it probably should. In general it&#8217;s possible to make many comments that swirl around religion and approach, one of the things that I&#8217;ve noticed is that wile Python has a much more disciplined developer community they&#8217;re not using this for the greater good.

Specifically, in looking at a benchmark that was posted, python was an order of magnitude (20 secs vs. 1 sec) slower than ruby. In investigating the performance bottleneck is the random module. This got me to think, why does python have &#8220;pickle&#8221; and &#8220;cPickle&#8221;? Comes down to lowest common denominator, or the inability for somebody to write an optimized package that can mimic a python package.

To that end why would somebody write big try catch blocks to see if modules exist and if they exist alias their names. Wouldn&#8217;t it be better if there was a way that if I have an &#8220;interface compatible&#8221; native (aka C) module that has better performance that there could be a way that python would give it preference.

e.g.

```
import random(version=1.2, lang=c)
```

or

```
# use the python version by default
import random(version=1.2, lang=py)   
```

or

```
#  use the latest version in the "fastest" code (C given preference)
import random     
```

where there could be a nice set of &#8220;standard&#8221; key value pairs that could provide addtional hints as to what language and version of a library was to be used.

**
  
Notes from the comp.lang.python discussion**

People fell into a few camps:

* There&#8217;s many &#8220;optimization&#8221; projects, like PyPy or ShedSkin (compile Python to C/C++ code).  In essence JIT the code, though not as passive as a true JIT.
* &#8220;most bottlenecks are from IO (disk, network) or interaction&#8221; so worrying about library performance is not worthwhile.
* Why worry about it, what we&#8217;ve got is good enough.

What amazes me is that time and time again, people don&#8217;t realize who their customers&#8217; are.  Languages like PHP realize their customers are hack VB programmers looking to build web pages.  So, having solid libraries and other things that can be totally abused (used) is a good use of &#8220;higher order design&#8221;.

In general, systems should support progressive improvement.  Somehow I fundamentally belive the python community doesn&#8217;t grasp that, but belive they&#8217;re building for themselves, not tools that enable a different class of engineer.
