---
title: Synergy is Fun
author: koblas
type: post
date: 2012-10-02T18:37:13+00:00
url: /p/synergy-is-fun/474
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 5617
dsq_thread_id:
  - 868492145
categories:
  - Ideas

---
One could say I&#8217;ve got too many projects with too much free time, but another way to look at things is that constant exploration can put a smile on your face.  I&#8217;ve been working on a few projects:

**GearTracker** ([http://geartracker.com**)**][1]

This is my big project, which I **really need **some product marketing help on.  I&#8217;ve gotten most of the infrastructure in place, but need somebody to come in an help me put the finishing 20% on top to make the first time experience right and probably catch where I&#8217;ve just been wrong headed about the thinking.

_Note &#8211; Really, could use help&#8230;_

**Spiro** (<https://github.com/koblas/spiro>)

One of the things that I keep on needing is a &#8220;midscale&#8221; web crawler. Would like to be able to crawl 100M pages without much thought along with obey all of robots.txt and be nice to sites, etc.etc.  What&#8217;s interesting is the crawler is the easy part, it&#8217;s being nice to sites that is difficult.

**Distal **(<https://github.com/koblas/distal>)

This is where synergies come from!  Originally I started Spiro with the idea of having a nice Bootstrap and Backbone UI, but it was klunky.  In one of those moments of frustration I started looking at EmberJS, which is way overkill&#8230; Ok, not really overkill, but not what I wanted.

So after looking at EmberJS I was inspired to produce a view framework that really tried to mimic the best parts, but keep the Backbone spirit alive.  Thus Distal was born.

What&#8217;s great is that I&#8217;ve had a chance to use it in GearTracker &#8211; which is where I&#8217;ve started to understand the whole client side UI development model, then take it back to Spiro to use again and break some of the ideas that I had in GearTracker.

**It&#8217;s all about Synergies!**

Ideas build on ideas, tools build on tools, those moments where you want a big old toggle switch to turn off your crawler can end up being 15 lines of JS (+15 of boilerplate) and 10 lines of Python.  And you&#8217;ve got a working control on a page, which does a real time refresh of the server to enable and disable things.

You did one of those &#8220;big deal&#8221; &#8211; but it is really a big deal &#8211; It&#8217;s not like I had to build a bunch of templates, do a full server reload of the page.  It&#8217;s a button it operates like a button.

 [1]: http://geartracker.com
