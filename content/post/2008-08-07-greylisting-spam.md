---
title: Greylisting spam…
author: koblas
type: post
date: 2008-08-07T18:06:51+00:00
url: /p/greylisting-spam/179
pvc_views:
  - 2691
dsq_thread_id:
  - 163814913
categories:
  - Development
tags:
  - greylist

---
I think I&#8217;ve now spent more time in my life than I ever want to think about fighting spam&#8230;&nbsp; I guess that has to do with spending the 20 years having some involvement in SMTP mail systems.&nbsp; Of course the stint writing the core infrastructure for MailFrontier&#8217;s anti-spam engine didn&#8217;t hurt my knowledge base.

My current pain is that I run a server that receives **lots** of spam, of course there is only three users on the whole machine.&nbsp; I think at last check I was getting over 500 pieces of spam a day.&nbsp; For years I&#8217;ve been reasonably happy with a well trained spamassassin setup, but recently that&#8217;s started failing.&nbsp; One of the technologies that I&#8217;ve not deployed for anti-spam is greylisting&#8230; So, here&#8217;s the notes about my days spent getting a good greylisting system in place.

Initial round:

**postgrey &#8211;** solid perl package, fairly basic in features, did cut down the flow from about 100 missed messages to 40.&nbsp; Very nice, but in the course of watching it for a few days noticed that a few classes of senders were making it through.&nbsp; Not it&#8217;s fault, but just a failure in greylisting.&nbsp; Note: Most of these were large clusters of hosts that are hosted at The Planet (ISP know for spam).

**greyboa &#8211;** my quick homebrew system based on postgrey (don&#8217;t ask, it was also a project to learn python asyncore/asynchat).&nbsp; Worked just about as well as postgrey.&nbsp;&nbsp; Moved it be based on SQLite since in one of the nightly postgrey runs the DB had some corruption which of course crashed the server and now I wasn&#8217;t getting any mail&#8230; sigh..

**sqlgrey &#8211;** The current experiment, not that I don&#8217;t like my code, but I&#8217;m going out of town for a few weeks and don&#8217;t want things to die while I&#8217;m not watching.&nbsp; Nice things:&nbsp; Better logging the postgrey/greyboa, it does some good sender (envelope level) matching to notice things like &#8216;+&#8217; addressing and Y!Groups unique sender patterns.&nbsp; Which should reduce the retry behavior a bit.

_Here&#8217;s my random comment ****_&#8212; I&#8217;m convinced that while spam is a problem, there has to be away to solve it&#8230;&nbsp;&nbsp; No, it&#8217;s impossible to not have unsolicited messages, but there should be some much better ways to take advantage of the fact that spammers must operate on a shotgun approach to sending messages.&nbsp; That shotgun leaves a lot of scatter&#8230;&nbsp; 

Fundamentally messages fall in a few buckets:

  * Immediate &#8212; communication between well known parties, with a long history
  * Unknown&nbsp; &#8212; messages between people who don&#8217;t have an established relationship, or little history
  * Junk&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &#8212; clearly &#8220;low priority&#8221; messages.

We should be able (greylisting is a good example) of delaying &#8220;unknown&#8221; messages for &#8220;long&#8221; periods of time until enough history has built up to re-bucket them into one of the other classes.&nbsp; That&#8217;s the basics of what I&#8217;m doing with greylisting, delay a message until RBL/Razor/Pyzor has a chance to build a little history before I delivery it to my mailbox&#8230;
