---
title: Splitting list interview question
author: koblas
type: post
date: 2011-03-14T20:41:40+00:00
url: /p/splitting-list-interview-question/350
aktt_notify_twitter:
  - yes
pvc_views:
  - 3379
aktt_tweeted:
  - 1
dsq_thread_id:
  - 253905483
categories:
  - Development
tags:
  - interview
  - python

---
Just made this up, feels like a good interview question

**Part 1 &#8211;** 

Write a function that takes a list and splits it at a specific percentage.

```python
f(mylist, pct) = list(mylist[0 ... len(mylist) * pct / 100.0],
                      mylist[len(mylist) * pct / 100.0 ... EOL])
```

**Part 2 &#8211;**

Now generalize that so that f(mylist, ..) takes an arbitrary number of percentages (in order) and returns you the list. This is interesting as an interview questions since I can see a bunch of interesting things coming up in the white board coding session.

* How to deal with short lists, more percentages than list items
* Approaches that end up with overlapping items (item #20 in the list twice)
* General familiarity of the language of choice
* How they understanding basic list processing &#8211; this is one list controlling the handling of another list.

Then again, somebody might pull a fast one on you and make you go huh?

```python
# python code
def split_list(mylist, *args):
    # ilist not necessary, but makes formatting easier
    ilist = map(lambda p : int(p * len(mylist) / 100.0), args) + [len(mylist)]
    return reduce(lambda l, v : [l[0] + [mylist[l[1]:v]], v], ilist, [[],0])[0]
```
