---
title: Fighting spam – greylisting take 2
author: koblas
layout: post
date: 2008-10-27T20:17:32+00:00
url: /p/fighting-spam-greylisting-take-2/193
aktt_tweeted:
  - 1
pvc_views:
  - 2381
dsq_thread_id:
  - 258675834
categories:
  - Development
tags:
  - spam
  - sqlgrey

---
You don&#8217;t really want to know, but I&#8217;ve spent my morning fighting spam.  It&#8217;s a periodic activity, makes me almost want to go back to the MailFrontier days when I could focus on these topics as a full time thing.  Though on the advantage side I can use a lot more off the shelf components in my battles.

If you recall I&#8217;ve been running sqlgrey on my box for a while, but over time more and more spam is getting through.  It&#8217;s primary objective is to slow down enough &#8220;unknown&#8221; email that other distributed sources will report on it&#8217;s true quality.  The problem is that looking at my logs that the spammers have worked out reasonable courses to get things routed onto white lists.

While I can&#8217;t say I&#8217;ve totally automated the process I&#8217;ve made one primary enhancement to sql grey which is adding a &#8220;BAD_IP&#8221; table which allows for either fully qualified IP addresses or /24 (Class C) versions of IP addresses to be added.   If an inbound message sources from one of these IP addresses then it&#8217;ll be &#8220;special&#8221;.  Two things happen with special IP addresses &#8211;  Longer greylisting cycle and they&#8217;re not allowed to be whitelisted.

The second part &#8212; which isn&#8217;t automated, today &#8212; is that my postfix log is chock full of all of the address probing going around.  So, all I need to look at is the IP addresses that are sourcing in lots and lots of probes.  If I see a lot of probes from your IP address you get added to the BAD_IP table.

Though as a feature request&#8230; I have a 60% solution in place, which is a python version of sqlgrey!  Not that I&#8217;m a big python person (ok, maybe converting slowly).  But, I&#8217;ve gotten to be a big OO person and procedural programming wrapped in a object wrapper is a bit &#8220;ugly&#8221;.
