---
title: Web 2.0 development – C++ vs. Java vs. PHP vs. Python
author: koblas
layout: post
date: 2008-04-12T17:53:09+00:00
url: /p/web-20-development-c-vs-java-vs-php-vs-python/141
pvc_views:
  - 76055
dsq_thread_id:
  - 160530545
categories:
  - General

---
Ok, it the last month I&#8217;ve used every one of these languages and most of them for the same project.&nbsp; Some highlights:

  * Java &#8212; decompilers are very useful in reverse engineering
  * C++ &#8212; std::string in naive use sucks for performance (wrote a pooled string ala Java String &#8212; performance increased by 10x)
  * Python &#8211; is easy to extend in C or C++
  * PHP &#8211; has the best web frameworks
  * Python &#8211; the spaces thing is prone to error, it really is hard to add addtional conditionals and insure that you got all of a if/for/&#8230; loop
  * PHP & Python &#8211; Lists are good as a basic structure
  * Python &#8211; As far as I can tell, it&#8217;s not a true lambda
  * PHP &#8211; Lax typing, both good and bad&#8230;
  * C++ &#8211; when it&#8217;s right, it rocks for performance
  * Java &#8211; a good way to rapidly build app and algs that work
  * Java &#8211; it&#8217;s easy to over object an API
  * C++ &#8211; boost is your friend, but it comes with a cost
  * Python &#8211; documentation is almost one step below C++ in quality &#8212; long topic around virtuous circles and how Java/PHP rock for docs.
  * Python &#8211; has the libraries that PHP only wishes it had, written by people who know what a library should look like.

What&#8217;s the upshot&#8230;

  * Use PHP to build web front ends &#8212; the ability to find a PHP programmer is pretty easy, odds are it&#8217;s not going to make/break your application.
  * Use simple RPC mechanisms (e.g. JSON RPC) to Python back ends for the heavy lifting &#8212; lots of choices here, but odds are it&#8217;s not going to make much difference.
  * Extend your Python with C++ for the computational parts of your heavy lifting &#8212; think peep hole optimization.

I used to think that using Java as a back end was the &#8220;only&#8221; way, but it&#8217;s more like the &#8220;cult of Java&#8221; vs. the &#8220;cult of &#8230;&#8221;, I&#8217;m not into religion just getting a job done.&nbsp;&nbsp; When it needs to be fast both languages will get it there, but you have to remember to spend your time optimizing only where it counts&#8230;
