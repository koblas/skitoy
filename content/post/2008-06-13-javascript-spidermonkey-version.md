---
title: JavaScript (spidermonkey) version
author: koblas
type: post
date: 2008-06-13T21:08:59+00:00
url: /p/javascript-spidermonkey-version/164
pvc_views:
  - 2080
dsq_thread_id:
  - 211124003
categories:
  - Development
tags:
  - python
  - performance

---
Way to carried away with this&#8230; here&#8217;s the SpiderMonkey version (as opposed to the rhino) one. Biggest complaint is the File object is a bit of a pain to use&#8230;

```python
fd = File('p.test');
fd.open("read",'text');

mre = /^__MULTI_TOKEN__\s+(\S+)\s+(.*)\t?\s*(\d+)\s*$/;
sre = /^__SINGLE_TOKEN__\s+(\S+)\s*\t?\s*(\d+)\s*$/;

var ofd = File('full.txt');
ofd.open('write,create,replace','text');
first = {}

while (line = fd.readln()) {
    if (m = line.match(mre)) {
        first[m[1]] = (first[m[1]] ? first[m[1]] : 0) + parseInt(m[3]);
        ofd.writeln(m[1] + " " + m[2] + "\t" + m[3]);
    } else if (m = line.match(sre)) {
        first[m[1]] = (first[m[1]] ? first[m[1]] : 0) + parseInt(m[2]);
    } else {
        print("Unknown: " + line);
    }
}

ofd.close()

ofd = File('first.txt');
ofd.open('write,create,replace','text');
for (key in first) { 
    ofd.writeln(key + "\t" + first[key]);
}
ofd.close()
```

This is all based on the [PHP/Perl/Python][1] performance code.

 [1]: /p/performance-of-python-php-and-perl/160
