---
title: head in python
author: koblas
type: post
date: 2012-03-06T15:45:42+00:00
url: /p/head-in-python/436
aktt_notify_twitter:
  - yes
pvc_views:
  - 4409
aktt_tweeted:
  - 1
dsq_thread_id:
  - 600930667
categories:
  - Development
tags:
  - python

---
Was going to post this to stackoverflow, but the question was deleted before I posted.

Turned out it was a fun exercise in writing a short program.

```python
def head(f_in, f_out, count=20):
    all([not f_out.write(l2) for l2 in [line for line in f_in][:count]])

head(open('/etc/passwd'), open('/tmp/p', 'w'), count=2)
```
