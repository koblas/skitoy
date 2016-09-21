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
  - General
tags:
  - java python php ruby

---
One of those moments where an interview question turns into a research project, or is it really a bake off?  The simple problem is demonstrate an algorithm to intersect two lists of numbers, fundamentally it&#8217;s a question about using modern interpreted languages and their associative array bits to make a simple intersection routine.  However many languages support many different ways to do things.  I&#8217;ve put together a test of Python vs. Java vs. Ruby vs. Perl vs. PHP and got a few interesting benchmarks.

Short Version of the results: java wins with python comming in second.

But, things are not so simple for instance there is a simple base approach (python example)

<pre lang="python">def isect(a, b) :
    o = []
    h = {}
    for i in a :
        h[i] = True
    for i in b :
        if h.get(i, False) :
            o.append(i)
    return o</pre>

or a more language unique version

<pre lang="python">def isect(a, b) :
    h = dict(iter([(i, True) for i in a]))
    return [i for i in b if h.get(i,False)]</pre>

or just using features of the language

<pre lang="python">def isect(a, b) :
    return list(set(a) & set(b))</pre>

All of these return the same result, but clearly we can think of this as a progression of an alorigthm.   Version 1 focusing on textbook to code, version 2 says there&#8217;s some cool language features and version 3 says, dude like don&#8217;t you _really_ know what your doing?

The upshot was that I sat down and wrote 12 different versions of this just to see what the language differences were.

<table border="0">
  <tr>
    <th>
      Language
    </th>
    
    <th>
      Version
    </th>
    
    <th>
      Alg. Time
    </th>
    
    <th>
      Run Time
    </th>
  </tr>
  
  <tr>
    <td>
      java
    </td>
    
    <td>
      1
    </td>
    
    <td>
      3.076
    </td>
    
    <td>
      5.888
    </td>
  </tr>
  
  <tr>
    <td>
      perl
    </td>
    
    <td>
      1
    </td>
    
    <td>
      3.622
    </td>
    
    <td>
      6.691
    </td>
  </tr>
  
  <tr>
    <td>
      php
    </td>
    
    <td>
      1
    </td>
    
    <td>
      3.901
    </td>
    
    <td>
      22.878
    </td>
  </tr>
  
  <tr>
    <td>
      python
    </td>
    
    <td>
      1
    </td>
    
    <td>
      1.740
    </td>
    
    <td>
      4.526
    </td>
  </tr>
  
  <tr>
    <td>
      ruby
    </td>
    
    <td>
      1
    </td>
    
    <td>
      3.517
    </td>
    
    <td>
      9.853
    </td>
  </tr>
  
  <tr>
    <td>
      java
    </td>
    
    <td>
      2
    </td>
    
    <td>
      0.817
    </td>
    
    <td>
      4.362
    </td>
  </tr>
  
  <tr>
    <td>
      python
    </td>
    
    <td>
      2
    </td>
    
    <td>
      3.550
    </td>
    
    <td>
      6.441
    </td>
  </tr>
  
  <tr>
    <td>
      ruby
    </td>
    
    <td>
      2
    </td>
    
    <td>
      7.984
    </td>
    
    <td>
      14.281
    </td>
  </tr>
  
  <tr>
    <td>
      python
    </td>
    
    <td>
      3
    </td>
    
    <td>
      1.500
    </td>
    
    <td>
      4.356
    </td>
  </tr>
  
  <tr>
    <td>
      ruby
    </td>
    
    <td>
      3
    </td>
    
    <td>
      3.809
    </td>
    
    <td>
      10.184
    </td>
  </tr>
  
  <tr>
    <td>
      c++
    </td>
    
    <td>
      1
    </td>
    
    <td>
      0.830
    </td>
    
    <td>
      1.209
    </td>
  </tr>
  
  <tr>
    <td>
      python
    </td>
    
    <td>
      4
    </td>
    
    <td>
      1.040
    </td>
    
    <td>
    </td>
  </tr>
  
  <tr>
    <td>
      php
    </td>
    
    <td>
      2
    </td>
    
    <td>
      2.000
    </td>
    
    <td>
    </td>
  </tr>
  
  <tr>
    <td>
      php
    </td>
    
    <td>
      3
    </td>
    
    <td>
      10.064
    </td>
    
    <td>
    </td>
  </tr>
  
  <tr>
    <td>
      java
    </td>
    
    <td>
      3
    </td>
    
    <td>
      3992.045
    </td>
    
    <td>
    </td>
  </tr>
</table>

Of course you&#8217;re probably wondering about language versions:

  * java 1.6.0
  * perl 5.8.8
  * php 5.2.9
  * python 2.5.4
  * ruby 1.8.6

<pre lang="java">// Java Version # 1
    private static int[] isect(int a[], int b[]) {
        int            l[] = new int[a.length];
        TreeMap        h = new TreeMap();
        int            idx = 0;

        for (int i = 0; i &lt; a.length; i++) {
            h.put(new Integer(a[i]), 1);
        }
        for (int i = 0; i &lt; b.length; i++) {
            if (h.containsKey(new Integer(b[i])))
                l[idx++] = b[i];
        }

        int o[] = new int[idx];
        for (int i = 0; i &lt; idx; i++) {
            o[i] = l[i];
        }

        return o;
    }
</pre>

<pre lang="perl"># Perl Version 1
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
</pre>

<pre lang="php"># PHP Version 1
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
</pre>

<pre lang="python"># Python Version 1
def isect(a, b) :
    o = []
    h = {}
    for i in a :
        h[i] = True
    for i in b :
        if h.get(i, False) :
            o.append(i)
    return o
</pre>

<pre lang="ruby"># Ruby Version 1
def isect(a, b)
  return a & b
end
</pre>

<pre lang="java">// Java Version 2
    private static Integer[] isect(Integer a[], Integer b[]) {
        ArrayList&lt;integer> l = new ArrayList&lt;/integer>&lt;integer>(a.length);
        HashSet&lt;/integer>&lt;integer>   h = new HashSet&lt;/integer>&lt;integer>();

        for (int i = 0; i &lt; a.length; i++) {
            h.add(a[i]);
        }
        for (int i = 0; i &lt; b.length; i++) {
            if (h.contains(b[i]))
                l.add(b[i]);
        }

        return (Integer[])l.toArray(new Integer[0]);
    }
</pre>

<pre lang="python"># Python Version 2
def isect(a, b) :
    h = dict(iter([(i, True) for i in a]))
    return [i for i in b if h.get(i,False)]
</pre>

<pre lang="ruby"># Ruby Version 2
def isect(a, b) 
  # Convert array to Set objects and perform intersection
  a = a.to_set
  b = b.to_set

  return a & b
end
</pre>

<pre lang="python"># Python Version 3
def isect(a, b) :
    return list(set(a)& set(b))
</pre>

<pre lang="ruby"># Ruby Version 3
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
end</pre>

<pre lang="php"># PHP Version 2
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
</pre>

<pre lang="php"># PHP Version 3
function isect($a, $b) {
    return array_intersect($a, $b);
}
</pre>

<pre lang="java">// Java Version 3
    private static Integer[] isect(Integer a[], Integer b[]) {
        Set&lt;integer> l = new HashSet&lt;/integer>&lt;integer>(Arrays.asList(a));
        l.retainAll(Arrays.asList(b));

        return (Integer[])l.toArray(new Integer[0]);
    }
&lt;/integer></pre>

<pre lang="python"># Python Version 4
def isect(a, b) :
    h = set(a)
    return [i for i in b if i in h]
</pre>

<pre lang="cpp">// C++ Version 1
std::list&lt;int>* isect(int len, int a[], int b[]) {
    __gnu_cxx::hash_set&lt;/int>&lt;int>   h = __gnu_cxx::hash_set&lt;/int>&lt;int>();

    for (int i = 0; i &lt; len; i++) 
        h.insert(a[i]);

    std::list&lt; int>   *l = new std::list&lt; int>();

    for (int i = 0; i &lt; len; i++) 
        if (h.find(b[i]) != h.end()) 
            l->push_back(b[i]);

    return l;
}
&lt;/int></pre>

Would enjoy peoples thoughts and feedback, or alternate implementations for these and other languages

</integer>