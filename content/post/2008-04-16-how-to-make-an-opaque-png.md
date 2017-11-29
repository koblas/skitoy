---
title: How to make an opaque PNG
author: koblas
type: post
date: 2008-04-16T22:04:31+00:00
url: /p/how-to-make-an-opaque-png/143
pvc_views:
  - 7743
dsq_thread_id:
  - 160531881
categories:
  - Development
tags:
  - notes
  - images

---
Needed an alpha channel PNG, didn&#8217;t want to fire up any real editor.

```bash
echo -n 'ccca' | tr ca '\377\200' &gt; t.rgba
convert -size 1x1 -depth 8 t.rgba opaque.png
```
