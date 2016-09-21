---
title: iPhone Objective-C bug?
author: koblas
layout: post
date: 2009-04-16T22:11:25+00:00
url: /p/iphone-objective-c-bug/225
aktt_tweeted:
  - 1
pvc_views:
  - 5648
dsq_thread_id:
  - 160531979
categories:
  - General

---
****<span class="fullpost">Funny bug from XCode and objective-c &#8230;<br /> </span>

**<span class="fullpost"><br /> warning: initialization from distinct Objective-C type </span>**

<span class="fullpost">For the following block of code:</span>**<span class="fullpost"><br /> </span>**

<pre>        // Quiz *qz = [[Quiz alloc] initFromDict: qdata];</pre>

<pre>        Quiz *quiz = [Quiz alloc];</pre>

<pre>        [quiz initFromDict: qdata];</pre>

From what I&#8217;ve read I ended up with the uncommented code as the operational code, since it implies that something bad will happen&#8230;  Before you ask &#8220;initFromDict&#8221; returns a (Quiz *) object..