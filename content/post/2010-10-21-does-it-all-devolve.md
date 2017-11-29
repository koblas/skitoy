---
title: Does it all devolve?
author: koblas
type: post
date: 2010-10-22T06:06:33+00:00
url: /p/does-it-all-devolve/330
aktt_notify_twitter:
  - no
pvc_views:
  - 4741
dsq_thread_id:
  - 160530640
categories:
  - Work
tags:
  - project


---
Had coffee with a friend recently and we drifted past the conversation of system designs. The crux is that we&#8217;ve both worked in organizations that are very bound to very large code bases&#8230; But, in many cases &#8212; products that have 100M+ users &#8212; they are monolithic piles of dung. Compile times that are non trivial, codebases that take minutes to startup, huge memory footprints. Systems that only survive because the DB is just a margin bigger than their usage.

Now as I set on on many other projects and build, code and create I have to wonder am I just creating the fore front of monolithic systems that will eventually succumb to the same pressures?  Or what internal force causes organizations to create &#8220;service oriented architectures&#8221; that have the loose coupling, but yet the high availability that is necessary to insure that you don&#8217;t need some HP NonStop system to keep your site running.  Is it force of will, design principals, or some bit of Computer Science DNA that isn&#8217;t taught?

I&#8217;ve gone off an seen the light of component systems, message queues and routers, design for failure, future proof APIs.   But, yet it&#8217;s something that people tend to turn up their noses at and go back to if it&#8217;s not integrated it doesn&#8217;t exist&#8230;

Other thoughts on how to create a culture that admires distributed simplicity?
