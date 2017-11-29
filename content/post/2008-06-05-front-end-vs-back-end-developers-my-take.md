---
title: Front-end vs. back-end developers (my take)
author: koblas
type: post
date: 2008-06-05T16:34:03+00:00
url: /p/front-end-vs-back-end-developers-my-take/157
pvc_views:
  - 64106
dsq_thread_id:
  - 160531890
categories:
  - Work
tags:
  - rant

---
Over on Dzone this article [Font-end vs. back-end developers][1] caught my attention.&nbsp; Alas, I feel compelled to write a longer rant.&nbsp; First off let&#8217;s touch on Mads points, but let me point out a bias first.

Front end devs tend to be less &#8220;classically&#8221; trained than back end devs, based on the resume flow I see for front end positions vs. back end positions front end developers come from non CS backgrounds, back end developers have CS degrees.

**Front-end devs don&#8217;t unit test**

While I can make an argument that the tools to test front end code vs. back end code are quite different, it&#8217;s a &#8220;cultural&#8221; thing more than an absolute.&nbsp; There are challenges, which is that to &#8220;front end test&#8221; code you need to have two computers with 6..7 different browsers attached, since unless you&#8217;re using some automated tools (which I&#8217;ve yet to find open sourced) there&#8217;s still the off chance that you&#8217;ve got a trailing &#8220;,&#8221; in some JavaScript to blow up the world.

Ultimately if you assume a level of &#8220;experience&#8221; it&#8217;s up to the senior people (maybe those people with CS degrees) to help set some standards and find tools to use in a production situation.

**Back-end devs are more low-level**

I can&#8217;t only partly disagree, since fundamentally, back-end can equate to everything from MySQL database table, index and query optimizations to multi-threaded queuing services.&nbsp; However this a false assumption, yes, those skills are needed but I&#8217;ve never met a true backend developer that really enjoyed dealing with the memory management issues in parsing XML from C++.&nbsp;&nbsp; It&#8217;s just tedious&#8230;&nbsp; much the same as matching layout in CSS between IE and FF.

**Front-end devs make more mistakes**

A joke, right&#8230;&nbsp; What you really should consider is a difference in tools, which relates to point #1 (unit tests).&nbsp; The biggest challenge is that &#8220;classic&#8221; backend is C++/Java or other compiled language.&nbsp; With a compiled language you have a greater chance that your code is meaningful (not error free), since a typo isn&#8217;t going to blow up later 

> had the following line in some PHP the other day:  
> &nbsp;&nbsp;&nbsp;&nbsp; throw new Foo\_Bar\_Exception();   
> problem was that it was a Foo\_Baz\_Exception();&nbsp; not caught until the line was executed

So while you might need to track down different classes of problems, you still have similar problems.&nbsp;&nbsp; While there is some &#8220;endorphin&#8221; driving development, the biggest challenge that a front-end developer has is that they know that once they&#8217;ve build out 90% of the functionality, that somebody is going to walk in and have them change 50% of the work they just did&#8230;&nbsp; Or potentially throw a re-design in the pipeline so, 90% of their work is out the window.&nbsp; Back end folks, just nod and smile and say &#8220;that&#8217;ll be 18 months of development&#8221;.

**Back-end devs hate the client-side**

Digging a hole for oneself&#8230;&nbsp; I think the problem is not that there is a dissatisfaction, but I&#8217;ve frequently encountered developers that are fairly rigid in their thinking (back end primarily and sometimes on the front end).&nbsp; The problem is that HTML/CSS browser compatibility is a shifting landscape, so what worked six months ago might be broken today.&nbsp; The idea that code without change can break is a tough concept to most developers.&nbsp; It&#8217;s a way of life for some and a battle to be fought for others.

**My personal take**

Again it&#8217;s a matter of training, some broad stroke generalizations:

**Front end developers** 

  * Typically don&#8217;t have a CS degree, or have a CS degree from a 3rd tier school.
  * Work in languages that similar to basic (see [PHP is Basic][2])
  * Have a visual skill in converting photoshop documents to CSS/HTML/etc.
  * Have a high tolerance for iterative programming, due to type free languages

**Back end developers**

  * Have a CS degree or _lots_ of experience 
  * Tend to me more systematic in their problem solving approach
  * Don&#8217;t mind spending days finding the one object that is leaking
  * Try and build tools to solve problems

Fundamentally, it&#8217;s up to senior developers to lead their teams to better solutions.&nbsp; Seniority comes from experience and education, but if you&#8217;re unwilling to learn new tools (NIH is evil) or help build tools to solve problems that are not necessarily your own, then you&#8217;re not senior.&nbsp; Your just another hack developer, who has a my way or the highway attitude.

 [1]: http://blog.madskristensen.dk/post/Front-end-vs-back-end-developers.aspx
 [2]: http://www.skitoy.com/p/plugg-the-decline-of-the-engineer/147
