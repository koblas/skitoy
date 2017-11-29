---
title: Python wierdness
author: koblas
type: post
date: 2010-08-30T18:43:02+00:00
url: /p/python-wierdness/301
pvc_views:
  - 3868
aktt_tweeted:
  - 1
dsq_thread_id:
  - 160532044
categories:
  - Development
tags:
  - python

---
Just frustrated, why the output is

Broken = 2 and Wierd = 3 at one level make no sense, since after all you would think that if you referenced a member variable it&#8217;s context would remain the same&#8230;

  
```python
class Foo :
    BROKEN = 1
    WIERD = 1

    def __init__(self) :
        print("Before broken=%d weird=%d" % (self.BROKEN, self.WIERD))
        self.BROKEN += 1
          
        self.__class__.WIERD += 1
        print("after broken=%d weird=%d" % (self.BROKEN, self.WIERD))

Foo()
Foo()

# Output is :
# Before broken=1 weird=1
# after broken=2 weird=2
# Before broken=1 weird=2
# after broken=2 weird=3
  
```
