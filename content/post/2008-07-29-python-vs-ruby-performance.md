---
title: Python vs. Ruby Performance
author: koblas
type: post
date: 2008-07-29T20:49:37+00:00
url: /p/python-vs-ruby-performance/172
pvc_views:
  - 25433
dsq_thread_id:
  - 160531921
categories:
  - Development
tags:
  - performance
  - python
  - java
  - ruby

---
Not sure why I&#8217;m spending the time on this problem, but it looked interesting.  For starters read a [Hacker&#8217;s News][1] article that mentioned Python vs. Ruby performance, which in turned liked to a [polish blog post][2].

The core of the blog post was this:

> 20 threads * 100,000 iterations
> 
>   1. Ruby 1.9 = 1.54 s.
>   2. Ruby Enterprise = 3.01 s.
>   3. JRuby 1.1.2 = 5.82 s.
>   4. Jython 2.2.1 = 11.86 s.
>   5. Python 2.5.2 = 12.32 s.
>   6. Ruby 1.8.7 = 22.68 s.

Which is totally amazing for a performance improvement stand point, but in digging further the original code is:

```python
from time import time
from random import Random
from threading import Thread
rand = Random().randint # alias

class Test(Thread):
   def __init__ (self):
      Thread.__init__(self)
      print "Starting %s" % self.getName()
   def run(self):
      a = [rand(0,SIZE) for x in xrange(SIZE)]
      a.sort()
      print "%s finished" % self.getName()

print "Start"
start = time()
THREADS, SIZE = 20, 100000
threads = []
for i in xrange(THREADS):
    t = Test()
    threads.append(t)
    t.start()
while True in [t.isAlive() for t in threads]:
    pass
print "Time: %s s" % (time() - start)
```

The first observation is that (unlike the ruby version) the python version has the overhead of a busy wait on the threads, so with than tiny fix (reduced runtime by 1 second)

```python
for t in threads :
    if t.isAlive() :
        t.join()
```

**Time: 17.6256890297 s**

Doing a quick decomposition of this, we really have a program that&#8217;s doing the following

```python
from time import time
from random import Random
rand = Random().randint # alias

THREADS, SIZE = 20, 100000

print "Start"
start = time()

for t in xrange(THREADS) :
      a = [rand(0,SIZE) for x in xrange(SIZE)]
      a.sort()

print "Time: %s s" % (time() - start)
```

**Time: 14.3786399364 s**

Not getting into numbers, but this executes in almost the same time as the threaded version&#8230; Hmm, so is the ruby version really all about &#8220;Threading Performance&#8221;? Can&#8217;t be, has to be either in the random or the loop&#8230; Lets look further.

```python
from time import time
from random import Random
rand = Random().randint # alias

THREADS, SIZE = 20, 100000

print "Start"
start = time()

for t in xrange(THREADS) :
      for x in xrange(SIZE) :
          rand(0,SIZE) 

print "Time: %s s" % (time() - start)
```

**Time: 10.9540541172 s**

There we have it, the rand() is taking 70% of the total time, while it does appear that the array append overhead is still 30% (~4 seconds) it&#8217;s at least useful to notice that there&#8217;s nothing that possible to improve it beyond this point.

**Conclusion:** Ruby might be faster, but to mix up a bunch of performance stats with threading is going to be problematic.

**Update:** In digging deeper python&#8217;s random number generator is written in python, thus of course it&#8217;s slow&#8230; It&#8217;s competing against a C version.

 [1]: http://news.ycombinator.com/item?id=260387
 [2]: http://blog.zabiello.com/articles/2008/07/26/threads-ruby-python
