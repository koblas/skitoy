---
title: Performance of Python, PHP and Perl
author: koblas
type: post
date: 2008-06-10T17:54:25+00:00
url: /p/performance-of-python-php-and-perl/160
pvc_views:
  - 55173
dsq_thread_id:
  - 160530565
categories:
  - Development
tags:
  - performance
  - perl
  - php
  - python

---
Had a 7GB text file that I needed to run some parsing on (to prepare for a DB import).&nbsp; As part of my habit I pulled out perl and whipped up a quick program to parse and generate some loadable files.&nbsp; While watching it run I got to thinking about &#8230; why &#8230; why perl (yes, I know habbits are hard to break).&nbsp; So while watching it run I re-wrote the program into PHP and Python. 

Performance Numbers (on 5 million lines worth of the file)

```
  $ time ./split.pl  p.test           # Perl 5.8.8

  real    0m38.577s
  user    0m33.554s
  sys     0m0.848s

  $ time ./split.py p.test            # Python 2.4.4
  real    0m44.895s
  user    0m42.975s
  sys     0m0.900s

  $ time php split.php p.test         # PHP 5.2.6RC4
  real    1m10.887s
  user    0m51.251s
  sys     0m18.677s
```

So, it appears that Perl is the right choice for this job.. Though python is a good second choice, but PHP 50% slower (most likely due to not having complied regular expressions).&nbsp;&nbsp; I also might note that I&#8217;m not fond of the python if/else probably with a chained expression match, where I want to &#8220;side effect&#8221; out the results of the match &#8212; is there better syntax? </p> 

Here&#8217;s the code for you&#8217;re viewing pleasure and possible commentary.

### perl

```perl
use strict;

my %first;

open(FULL, ">full.txt");

while (<>) {
# __SINGLE_TOKEN__ adrianenamorado                 1
# __MULTI_TOKEN__ a aaron yalow        1
    chop;
    if (/^__MULTI_TOKEN__\s+(\S+)\s+(.*)\t?\s*(\d+)\s*$/) {
        $first{$1} += $3;
        print FULL  $1," ", $2, "\t", $3, "\n";
    } elsif (/^__SINGLE_TOKEN__\s+(\S+)\s*\t?\s*(\d+)\s*$/) {
        $first{$1} += $2;
    } else {
        print "Unknown: ", $_, "\n";
    }
}

close(FULL);

open(FIRST, ">first.txt");
while (my($k, $c) = each %first) {
    print FIRST $k,"\t",$c,"\n";
}
close(FIRST);
```

## python 

```python
import sys, os, re

first = dict()

ofd = open("full.txt", 'w')

mre = re.compile('^__MULTI_TOKEN__\s+(\S+)\s+(.*)\t?\s*(\d+)\s*$')
sre = re.compile('^__SINGLE_TOKEN__\s+(\S+)\s*\t?\s*(\d+)\s*$')

ifd = open(sys.argv[1], 'r')

for line in ifd :
    line = line.strip()
    m = mre.match(line)
    if m :
        first[m.group(1)] = m.group(3)
        print >> ofd, m.group(1), " ", m.group(2), "\t", m.group(3)
    else :
        m = sre.match(line)
        if m :
            first[m.group(1)] = m.group(2)
        else :
            print "Unknown ", line

ofd.close();

ofd = open("first.txt", 'w')
for (k, c) in first.iteritems() :
    print >> ofd, k, "\t", c
ofd.close()
```

### php

```php
$first = array();

$fd = fopen("full.txt", 'w');
$in = fopen($argv[1], 'r');

while ($line = fgets($in)) {
    $line = trim($line);
    if (preg_match('/^__MULTI_TOKEN__\s+(\S+)\s+(.*)\t?\s*(\d+)\s*$/', $line, $m)) {
        $first[$m[1]] += $m[3];
        fprintf($fd, "%s %s\t%d\n", $m[1], $m[2], $m[3]);
    } else if (preg_match('/^__SINGLE_TOKEN__\s+(\S+)\s*\t?\s*(\d+)\s*$/', $line, $m)) {
        $first[$m[1]] += $m[2];
    } else {
        print "Unknown: {$line}\n";
    }
}

fclose($fd);

$fd = fopen("first.txt", 'w');
foreach ($first as $k => $c) {
    fprintf($fd, "%s\t%d\n", $k, $c);
}
fclose($fd);
```
