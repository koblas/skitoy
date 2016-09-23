---
title: Chicken Scratches on Crawler
author: koblas
layout: post
date: 2012-07-20T16:09:36+00:00
url: /p/chicken-scratches-on-crawler/466
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 5352
dsq_thread_id:
  - 773472429
categories:
  - Development
tags:
  - crawler

---
(More notes to myself)

Inspired by CommonCrawl, but their data isn&#8217;t all that I want.  After building out my redback system, which I&#8217;ve now let sit and die for the last two years (it worked, but had some small scaling issued).  Revised idea based on some of the CommonCrawl thinking&#8230;

&#8212; **Fetcher**

Built in Tornado, with a simple way to dequeue objects from the store, running multiple async fetches.  Once an object is fetched have a simple XPath that can extract secondary real-time fetch objects (e.g Images that are interesting).  Store everything in the **Store**.

&#8212; **Store**

For now either Riak or Mongo &#8211; with a mapper.

&#8212; **Mapper**

Sort through all of the &#8220;non-processed&#8221; documents and extract links based on frequency.

&#8212; TODO &#8211; find reference to CommonCrawl doc.

Basic Process &#8211; The first interations will take a &#8220;long&#8221; time to iterate, but as the schedule table fills the fetcher will always be busy.

  * Seed with one URL in the &#8220;todo&#8221; table
  * Fetch and Store (with robots.txt check)
  * Map over the data to extract more pages to fetch store these in the &#8220;todo&#8221; table, check to insure that the page isn&#8217;t fetched store in the &#8220;todo&#8221; table.
  * REPEAT

Now the &#8220;blob&#8221; table will be full on HTML (and Image) documents that can be used in any way that one wants.

**Blob Table &#8211;**

  * URL
  * Time Fetched
  * Body MD5
  * Headers
  * Body

**Schedule Table &#8211;**

  * URL
  * Time Inserted
  * Reference Count (e.g. PageRank)

&nbsp;
