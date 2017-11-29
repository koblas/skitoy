---
title: Love/Hate with python
author: koblas
type: post
date: 2008-03-28T20:12:37+00:00
url: /p/lovehate-with-python/139
pvc_views:
  - 2734
dsq_thread_id:
  - 183898167
categories:
  - Development
tags:
  - rant

---
**Hate &#8212;** some of the modules, gadzooks people get a clue:

  * html2text uses the SGML parser, so &#8220;normal&#8221; HTML will fail

After fixing it up to use HTMLParser .. it still sucks!&nbsp; HTML parser is built using regular expressions, well guess what&#8230; bad HTML still fails.

**Love** &#8212; Had a HTML=>Text converter laying around in C++ took all of 30 minutes to wire it into python.&nbsp; It works&#8230;
