---
title: iPhone Objective-C bug?
author: koblas
type: post
date: 2009-04-16T22:11:25+00:00
url: /p/iphone-objective-c-bug/225
aktt_tweeted:
  - 1
pvc_views:
  - 5648
dsq_thread_id:
  - 160531979
categories:
  - Development
tags:
  - xcode

---
Funny bug from XCode and objective-c &#8230;

** warning: initialization from distinct Objective-C type **

For the following block of code:

```
// Quiz *qz = [[Quiz alloc] initFromDict: qdata];

Quiz *quiz = [Quiz alloc];

[quiz initFromDict: qdata];
```

From what I&#8217;ve read I ended up with the uncommented code as the operational code, since it implies that something bad will happen&#8230;  Before you ask &#8220;initFromDict&#8221; returns a (Quiz *) object..
