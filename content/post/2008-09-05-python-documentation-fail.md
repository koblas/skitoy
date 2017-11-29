---
title: Python Documentation — Fail!
author: koblas
type: post
date: 2008-09-05T18:35:43+00:00
url: /p/python-documentation-fail/185
aktt_tweeted:
  - 1
pvc_views:
  - 2844
dsq_thread_id:
  - 160531930
categories:
  - Development
tags:
  - python
  - rant

---
One of many rants against python documentation.  Fundamentally, things like this only re-enforce why it didn&#8217;t receive the rapid acceptance of PHP.

$ pydoc list

```
...
| index(...)
| L.index(value, [start, [stop]]) -&gt; integer -- return first index of value</pre>
...
```

Ok, that&#8217;s good&#8230; But what about the &#8220;not found&#8221; case, is it documented, nope!  We have three choices, can you pick the right one?

  * Return **None**
  * Return **-1**
  * Throw an exception

So, what the documentation **requires** you to do is write three lines of code to understand how list.index() works.  This is fundamental failure of the maintainers of the language.
