---
title: Python Lazy Object Reloader
author: koblas
layout: post
date: 2011-10-18T21:03:46+00:00
url: /p/python-lazy-object-reloader/394
aktt_notify_twitter:
  - yes
pvc_views:
  - 4300
aktt_tweeted:
  - 1
dsq_thread_id:
  - 447143282
categories:
  - Development
tags:
  - python

---
I&#8217;m sure there&#8217;s a more general title for this kind of object, but the challenge came up and here&#8217;s what I put together.  The basic idea is to have a python class that only recomputes something hard when one of the attributes is modified.  It doesn&#8217;t make sense to recompute on every modification, nor does it make sense to recompute if it&#8217;s never read.

In all cases, here&#8217;s the code sample.  I&#8217;m sure it&#8217;ll be useful on stackoverflow someday.

```python
#
#  Decorator that takes a list of members that are cached
#
def second_cache(members=None) :
    def inner(cls) :
        cls._second_cache_dirty = False

        if members is None :
            def setter(self, name, value) :
                if name not in ('_second_cache_dirty', ) :
                    self._second_cache_dirty = True
                return object.__setattr__(self, name, value)
        else :
            cls._second_cache_members = set(members)
            def setter(self, name, value) :
                if name in cls._second_cache_members and name not in ('_second_cache_dirty',):
                    self._second_cache_dirty = True
                return object.__setattr__(self, name, value)

        cls.__setattr__ = setter

        return cls
    return inner

#
#  A revised property decorator that checkes the cacheable state of an object and
#   calls refresh if defined and needed
#
def cache_prop(func) :
    def call_me(self) :
        if self._second_cache_dirty :
            if hasattr(self, '_refresh') :
                self._refresh()
                self._second_cache_dirty = False
        return func(self)
    return property(call_me)

#
# Test class to demonstrate that only if the member bar is modified that the object
#  calls the refresh method.
#
@second_cache(members=['bar'])
class Test(object) :
    def __init__(self) :
        self.bar = 1
        self.cat = 2
        self.dog = 3
        self.baz = 4

    def _refresh(self) :
        print "Cache Dirty - need to refresh object"

    @cache_prop
    def frog(self) :
        return self.bar + self.cat

    def fun(self) :
        print "BigTop"

t1 = Test()

print "Dirty:", t1.frog
t1.bar = 7
print "Dirty:", t1.frog
print "Clean:", t1.frog
```
