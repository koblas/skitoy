---
title: FizzBuzz of the day
author: koblas
layout: post
date: 2016-07-05T20:29:07+00:00
url: /p/fizzbuzz-of-the-day/618
pvc_views:
  - 261
dsq_thread_id:
  - 4963290442
categories:
  - Development
tags:
  - fizzbuzz

---
Like many pieces of code, there is always a story behind it.

Your FizzBuzz solutions of the day &#8211; using operator precedence to get a result

```python
for num in xrange(1,101):
    print 'Fizz' if not num % 3 else '' + 'Buzz' if not num % 5 else '' or num
```

Or on one line.

```python
print '\n'.join('Fizz' if not i % 3 else '' + 'Buzz' if not i % 5 else '' or str(i) for i in range(1,101))
```

&nbsp;
