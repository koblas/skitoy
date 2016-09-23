---
title: Continuous Integration Process
author: koblas
layout: post
date: 2015-06-19T17:02:27+00:00
url: /p/continuous-integration-process/582
pvc_views:
  - 942
dsq_thread_id:
  - 3862351097
categories:
  - Development
tags:
  - project management

---
Was at a wonderful conference hosted by one of Tubular&#8217;s investors (FirstMark) where VPE&#8217;s, CTOs and key technical leads got together from a bunch of their investments to listen to speakers and have some good round table discussions.  I spent my time participating in a round table on development processes, which evolved quickly from &#8220;life is good&#8221; to &#8220;here is a rough spot we&#8217;re having&#8217;. It&#8217;s really refreshing to have honest communication about your problems rather than having to wear the customer facing hat of the world is perfect and of course we will meet your every need.  _Note; Customers we do meet your ever need, sometimes the process is less than perfect to get there._

As we were wrapping up and went to grab buffet lunch. Was chatting about what we would do sooner now that we have a bit of perspective on what it takes to go from two people at a desk with an idea, to an organization.  What&#8217;s interesting is that we all agreed that putting Continuous Integration into the process earlier would be better, while this means different things to different people.  At the core &#8212;

  1. Setting up git auto builds with [TravisCI][1] &#8211; everybody thought that was the best place to start, with migration to [Jenkins][2] as inevitable
  2. Getting Unit Testing / Integration Testing in place
  3. Getting Continuous Deployment working

Having those three things early in an organization will help lay the fundamentals of a culture that will be more agile and able to iterate faster as the company grows.

Having the first two are bread-and-butter in the modern development practices, having Continuous Deployment is the big nut.  Why? It ensures that the responsibility for delivering quality code never leaves the engineering organization, that makes sure you stay agile.  The moment you introduce QA you will always have large releases, now you have a bottleneck on what goes out and lots of finger pointing at who is responsible.

**Question: **Who is responsible for code quality?
  
**Answer: **Engineering

As leadership in engineering my goal is to make sure that we understand that is our commitment.  So setting up tools early to make it easier to grow cannot be underestimated.

 [1]: https://travis-ci.org/
 [2]: https://jenkins-ci.org/
