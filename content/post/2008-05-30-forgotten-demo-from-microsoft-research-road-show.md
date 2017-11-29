---
title: Forgotten demo from Microsoft Research Road Show
author: koblas
type: post
date: 2008-05-30T15:54:12+00:00
url: /p/forgotten-demo-from-microsoft-research-road-show/154
pvc_views:
  - 2039
dsq_thread_id:
  - 249142878
categories:
  - General

---
My spouse pointed me at an appliance product the other day that is pretty much a package of network probing tools ([Qualys][1]).&nbsp; Their niche is having a product that probes a network of vulnerabilities before somebody else can exploit them.&nbsp; Good idea, simple product, easy updates, etc. etc.&nbsp;&nbsp; Makes total sense since many &#8220;technical&#8221; people don&#8217;t like dealing with software updates and upgrades, it provides an appliances computer that somebody else &#8220;manages&#8221; &#8230; &#8220;updates&#8221; that can reside on your network.

Reminds me of MailFrontier, we started out as a software company, but it turns out that IT likes appliances since it means that the don&#8217;t need to &#8220;manage&#8221; another computer, just complain at a vendor.

Appliance?&nbsp; Microsoft Research?&nbsp; What?

While it wasn&#8217;t a &#8220;demo&#8221; at the MS SV Research Roadshow, it&#8217;s clearly a feature that needs to be added to this appliance.&nbsp; Which is instead of being a pure probe system, it should be an active monitor.&nbsp; MS demonstrated a research project that would look at your network an notice the true dependencies (Exchange which specific AD hosts, etc.), these hosts on that file server.&nbsp; So, when things go wrong, you can go look at a real picture (not the network diagram that hasn&#8217;t been updated) at what really is depending on what and it can show that this AD server that is down, was really the only one that your Exchange server knew about (somebody forgot to update a configuration) and of course this is what&#8217;s causing you grief.&nbsp; Much faster than spending 30 minutes rebooting machines until they&#8217;re fixed.

Sounds like a simple growth from &#8220;Probe Monitor&#8221; to &#8220;Active discovery and mapping&#8221;&#8230;

 [1]: http://www.qualys.com
