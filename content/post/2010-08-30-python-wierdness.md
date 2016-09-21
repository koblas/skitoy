---
title: Python wierdness
author: koblas
layout: post
date: 2010-08-30T18:43:02+00:00
url: /p/python-wierdness/301
pvc_views:
  - 3868
aktt_tweeted:
  - 1
dsq_thread_id:
  - 160532044
categories:
  - General
tags:
  - python

---
Just frustrated, why the output is

Broken = 2 and Wierd = 3 at one level make no sense, since after all you would think that if you referenced a member variable it&#8217;s context would remain the same&#8230;

[code]
  
class Foo :
      
BROKEN = 1
      
WIERD = 1

def \_\_init\_\_(self) :
          
print(&#8216;Before broken=%d weird=%d&#8217; %( self.BROKEN, self.WIERD))
          
self.BROKEN += 1
          
self.\_\_class\_\_.WIERD += 1
          
print(&#8216;after broken=%d weird=%d&#8217; %( self.BROKEN, self.WIERD))

Foo()
  
Foo()

\# Output is :
  
\# Before broken=1 weird=1
  
\# after broken=2 weird=2
  
\# Before broken=1 weird=2
  
\# after broken=2 weird=3
  
[/code]