---
title: When’s a string not a string
author: koblas
layout: post
date: 2008-06-13T18:23:26+00:00
url: /p/whens-a-string-not-a-string/162
pvc_views:
  - 2470
categories:
  - General

---
<p dir="ltr" style="margin-right: 0px">
  <strong>When it&#8217;s intertwined</strong> &#8212; ok, bad joke.
</p>

I&#8217;m currently &#8220;fighting&#8221; (playing) around with the [python storm][1] ORM system and had the following problem (not the real code, but demonstration).

What I wanted to say is:

```
find(..., employee_title == 'CEO')
```

However this didn&#8217;t work, I had to say:

```
find(..., employee_title == u'CEO')
```

After a bit of discussion down a mailing list, I got the &#8220;classic&#8221; answer back.

Maybe you think it&#8217;s annoying, but it&#8217;s correct, and doing it with automatic conversion is error-prone.

While I can see the point, it&#8217;s one of my pet peeves with Python specifically&#8230; Which is that there are quite a few programmers who are overly type aware, but yet are working in a language that is &#8220;late typing&#8221;.&nbsp;&nbsp; You would think that in a world where one of the contributions to design is duck typing, would be the idea that last mile type enforcement is a bad thing.

What&#8217;s really funny is that when you put this in context of this post I read this morning [about 100% code coverage][2] the following can be observed.

To simply state a goal of 100% code coverage for a test suite in the presence of late typing is a red herring.&nbsp; 

```python
def foo(flg) :
   if flg :
       x = u'TEST'
   else :
       x = 'TEST'

def bar(i) :
   x = ""
   x += foo(False)
   return x
   
def unitTest() : 
  j = foo(True)
  for i in range(1,3) :
     k = bar(i)
```

I&#8217;ve got 100% code coverage in (flawed) unit test, but the problem is that since the typing is late there is the potential for lots of latent bugs. Eiffel! Since python isn&#8217;t going to give into true typing, it might as well adopt [PEP 316: Programming by Contract][3] to enable a test suite to enforce pre/post conditions to insure a function can only return specific types. 

Parting thought after I did a bit of investigation: [Python Contracts][4] &#8211; plus it improves the documentation of functions (another personal pain point)

 [1]: https://storm.canonical.com/
 [2]: http://blog.obishawn.com/2008/06/why-you-should-have-100-code-test.html
 [3]: http://www.python.org/dev/peps/pep-0316/
 [4]: http://www.wayforward.net/pycontract/
