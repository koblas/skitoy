---
title: Performance of JavaScript object reduce
author: koblas
layout: post
date: 2018-02-03T18:53:38+00:00
url: /p/performance-of-javascript-object-reduce/642
categories:
  - technical

---


## Performance of JavaScript object reduce

Just a short post to look at assumptions. A few weeks ago was having one of those classic debates with a co-worker about the performance of object construction. Since with ES6 it is very easy to write:

```
const obj = data.reduce((acc, [k, v]) => ({ ...acc, [k]: v }), {});
```

I had internally always made the assumption that JavaScript's runtime was making some [tail call](https://en.wikipedia.org/wiki/Tail_call) style optimizations on object reduce. But, after the discussion I realized that you should measure and not assume.

So measure we did, only to find that while it's short in syntax it's slow in performance:


| Function | 10 items | 100 items | 1000 items | 10000 items |
|---|---:|---:|---:|---:|
| reduceHead | 0.094276 | 1.056871 | 113.687105 | 11013.714067 |
| reduceTail | 0.117997 | 1.777858  | 110.682865 | 11794.382281 |
| reduceAssign | 0.090573 | 0.161337 | 0.420563 | 2.184986 |

_This is on the 8.9.0 node runtime. All times are in 'ms'_

What you can see is this is pretty close to a exponentail growth based on the number of items. Sure it's fast enough if it's a small object (~10 items) but, very quickly grows if it's anything of size.

The test program (run at each of the different input counts)

```
const {
  performance,
  PerformanceObserver
} = require('perf_hooks');

/*
** Construct some test data
*/
const data = [];

for (let i = 0; i < 1000; i ++) {
  data.push([String(i), i]);
}

/*
**  Test variations
*/
function reduceHead() {
  return data.reduce((acc, [k, v]) => ({ ...acc, [k]: v }), {});
}

function reduceTail() {
  return data.reduce((acc, [k, v]) => ({ [k]: v, ...acc }), {});
}

function reduceAssign() {
  return data.reduce((acc, [k, v]) => {
    acc[k] = v;
    return acc;
  }, {});
}

/*
**  Performance hooks
*/
const obs = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  console.log(entries[0].name, entries[0].duration, 'ms');
});

const wrapHead = performance.timerify(reduceHead);
const wrapTail = performance.timerify(reduceTail);
const wrapAssign = performance.timerify(reduceAssign);

obs.observe({ entryTypes: ['function'] });

wrapHead();
wrapTail();
wrapAssign();

```
