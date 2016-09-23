---
title: Array Intersection Bake-off
author: koblas
layout: post
date: 2009-05-15T17:18:05+00:00
url: /p/array-intersection-bake-off/236
aktt_tweeted:
  - 1
pvc_views:
  - 16179
dsq_thread_id:
  - 160531997
categories:
  - Development
tags:
  - performance
  - java 
  - python 
  - php 
  - ruby

---
One of those moments where an interview question turns into a research project, or is it really a bake off?  The simple problem is demonstrate an algorithm to intersect two lists of numbers, fundamentally it&#8217;s a question about using modern interpreted languages and their associative array bits to make a simple intersection routine.  However many languages support many different ways to do things.  I&#8217;ve put together a test of Python vs. Java vs. Ruby vs. Perl vs. PHP and got a few interesting benchmarks.

Short Version of the results: java wins with python comming in second.

But, things are not so simple for instance there is a simple base approach (python example)

```python
def isect(a, b) :
    o = []
    h = {}
    for i in a :
        h[i] = True
    for i in b :
        if h.get(i, False) :
            o.append(i)
    return o
```

or a more language unique version

```python
def isect(a, b) :
    h = dict(iter([(i, True) for i in a]))
    return [i for i in b if h.get(i,False)]
```

or just using features of the language

```python
def isect(a, b) :
    return list(set(a) & set(b))</pre>
```

All of these return the same result, but clearly we can think of this as a progression of an alorigthm.   Version 1 focusing on textbook to code, version 2 says there&#8217;s some cool language features and version 3 says, dude like don&#8217;t you _really_ know what your doing?

The upshot was that I sat down and wrote 12 different versions of this just to see what the language differences were.

Language  |  Version    | Alg. Time     | Run Time
----------|-------------|---------------|------
java      |  1          | 3.076         | 5.888
perl      |  1          | 3.622         | 6.691
php       |  1          | 3.901         | 22.878
python    |  1          | 1.740         | 4.526
ruby      |  1          | 3.517         | 9.853
java      |  2          | 0.817         | 4.362
python    |  2          | 3.550         | 6.441
ruby      |  2          | 7.984         | 14.281
python    |  3          | 1.500         | 4.356
ruby      |  3          | 3.809         | 10.184
c++       |  1          | 0.830         | 1.209
python    |  4          | 1.040   
php       |  2          | 2.000   
php       |  3          | 10.064  
java      |  3          | 3992.045    

Of course you&#8217;re probably wondering about language versions:

  * java 1.6.0
  * perl 5.8.8
  * php 5.2.9
  * python 2.5.4
  * ruby 1.8.6

```java
// Java Version # 1
    private static int[] isect(int a[], int b[]) {
        int            l[] = new int[a.length];
        TreeMap        h = new TreeMap();
        int            idx = 0;

        for (int i = 0; i < a.length; i++) {
            h.put(new Integer(a[i]), 1);
        }
        for (int i = 0; i < b.length; i++) {
            if (h.containsKey(new Integer(b[i])))
                l[idx++] = b[i];
        }

        int o[] = new int[idx];
        for (int i = 0; i < idx; i++) {
            o[i] = l[i];
        }

        return o;
    }
```

```perl
# Perl Version 1
sub isect {
    my($a, $b) = @_;
    my(@o, %h);

    for my $i (@$a) {
        $h{$i} = 1;
    }
    for my $i (@$b) {
        push(@o, $i) if $h{$i};
    }

    return @o;
}
```

```php
# PHP Version 1
function isect($a, $b) {
    $h = array();
    $o = array();

    foreach ($a as $i) {
        $h[$i] = true;
    }
    foreach ($b as $i) {
        if ($h[$i]) {
            array_push($o, $i);
        }
    }

    return $o;
}
```

```python
# Python Version 1
def isect(a, b) :
    o = []
    h = {}
    for i in a :
        h[i] = True
    for i in b :
        if h.get(i, False) :
            o.append(i)
    return o
```

```ruby
# Ruby Version 1
def isect(a, b)
  return a & b
end
```

```java
// Java Version 2
    private static Integer[] isect(Integer a[], Integer b[]) {
        ArrayList<integer> l = new ArrayList</integer><integer>(a.length);
        HashSet</integer><integer>   h = new HashSet</integer><integer>();

        for (int i = 0; i < a.length; i++) {
            h.add(a[i]);
        }
        for (int i = 0; i < b.length; i++) {
            if (h.contains(b[i]))
                l.add(b[i]);
        }

        return (Integer[])l.toArray(new Integer[0]);
    }
```

```python
# Python Version 2
def isect(a, b) :
    h = dict(iter([(i, True) for i in a]))
    return [i for i in b if h.get(i,False)]
```

```ruby
# Ruby Version 2
def isect(a, b) 
  # Convert array to Set objects and perform intersection
  a = a.to_set
  b = b.to_set

  return a & b
end
```

```python
# Python Version 3
def isect(a, b) :
    return list(set(a)& set(b))
```

```ruby
# Ruby Version 3
def isect(a, b) 
    o = Array.new
    h = Hash.new

    a.each do |i|
        h[i] = 1
    end
    b.each do |i|
        if h[i] 
            o.push(i)
        end
    end

    return o
end
```

```php
# PHP Version 2
function isect($a, $b) {
    $b = array_flip($b);
    $o = array();

    foreach ($a as $i) {
        if(isset($b[$i])) {
            $o[] = $i;
        }
    }

    return $o;
}
```

```php
# PHP Version 3
function isect($a, $b) {
    return array_intersect($a, $b);
}
```

```java
// Java Version 3
    private static Integer[] isect(Integer a[], Integer b[]) {
        Set<integer> l = new HashSet</integer><integer>(Arrays.asList(a));
        l.retainAll(Arrays.asList(b));

        return (Integer[])l.toArray(new Integer[0]);
    }
```

```python
# Python Version 4
def isect(a, b) :
    h = set(a)
    return [i for i in b if i in h]
```

```c++
// C++ Version 1
std::list<int>* isect(int len, int a[], int b[]) {
    __gnu_cxx::hash_set</int><int>   h = __gnu_cxx::hash_set</int><int>();

    for (int i = 0; i < len; i++) 
        h.insert(a[i]);

    std::list< int>   *l = new std::list< int>();

    for (int i = 0; i < len; i++) 
        if (h.find(b[i]) != h.end()) 
            l->push_back(b[i]);

    return l;
}
```

Would enjoy peoples thoughts and feedback, or alternate implementations for these and other languages
