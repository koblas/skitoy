---
title: Good programmers are lazy programmers
author: koblas
type: post
date: 2008-03-03T18:28:31+00:00
url: /p/good-programmers-are-lazy-programmers/135
pvc_views:
  - 2035
dsq_thread_id:
  - 182886511
categories:
  - Development

---
Good programmers enjoy working, they just don&#8217;t like re-inventing the wheel.&nbsp; There is a whole class of programmers who suffer from NIH (not invented here) who then dutifully re-invent, re-write, re-build a system.&nbsp; Some of them are even so &#8220;wise&#8221; to re-use standard nomenclature in their re-inventions that when they present the XYZ project they can proclaim that they&#8217;re using ABC technology.&nbsp; However they fail to mention that the ABC technology is not the industry standard but a system of their own design.&nbsp; Which of course means that nobody on earth (outside of one or two engineers) can support it, modify it or change it.

Good programmers look a problem figure out how to leverage the most out of a community &#8212; open source rocks &#8212; and solve the problems that the need to solve.&nbsp; Most of the time the open source system doesn&#8217;t meet 100% of the requirements, or requires a specific way of thinking about the problem.&nbsp; Which is a small cost to pay in terms of overall productivity.

Example &#8212; When I started at Wink we had no MVC framework for our PHP infrastructure.&nbsp;&nbsp; So took a quick look around and not seeing anything that was quite a match to our problem, went off and wrote something that was a closer match to our needs.&nbsp; Time passed, the MVC frameworks got better, more features, etc., etc.&nbsp; Ours of course was getting cruftier and was showing a general lack of thought (it started as a three day hack).&nbsp;&nbsp; There was a very painful moment, when I said that we needed to move to a open source solution for our MVC bits&#8230;&nbsp; pain &#8230;&nbsp;&nbsp; But after a few days of having people learn a new approach to problem productivity increased and now we have a much more scalable approach to the problem.

Did I suffer from NIH at the inception?&nbsp; Or can I say that I did a detailed analysis of the alternatives?&nbsp;&nbsp; Maybe, maybe not.&nbsp; At the end of the day, I&#8217;m happy moving to a standard solution if it meets 90% of my needs (if it met 100% of my needs, I wouldn&#8217;t have a job).&nbsp;&nbsp; What drives me batty is programmers who believe that there is only one way, their way, to solve a problem and not embrace the work of the community.
