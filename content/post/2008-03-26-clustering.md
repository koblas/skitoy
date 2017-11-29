---
title: Clustering …
author: koblas
type: post
date: 2008-03-26T15:48:09+00:00
url: /p/clustering/137
pvc_views:
  - 2464
dsq_thread_id:
  - 347206128
categories:
  - Development
tags:
  - clustering
  - nlp

---
I&#8217;ve been playing with clustering my email, just a sample set of 300 or so messages.&nbsp; It&#8217;s been a while since I&#8217;ve done any &#8220;NLP&#8221; work and it&#8217;s really quite fun.

Some learnings:

As the dimentionality of space increases everything starts to sit at the origin:

  * initially you might have 120 unique words in an email message, some of which are repeated multiple times (e.g. &#8220;the&#8221;, &#8220;linkedin&#8221;, &#8230;)
  * but, a second email message might have a different set of 120 words, with an overlap of 40..
  * hang on a second, those 40 words most of them are stop words on words that have an overall corpus frequency that is quite high. 
  * Solutions:&nbsp; Stemming and Eliminating stop words, or more&#8230; 

Two useful papers&#8230;

  * [Using TF-IDF Anomalies to Cluster Documents on Subject Matter][1]
  * [Simultaneous Categorization of Text Documents and Identification of Cluster-dependent Keywords][2]

Totally useful resource for clustering and text categorization:

[http://www.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/][3]

 [1]: http://aser.ornl.gov/students/WhitneyPresentation082007.ppt
 [2]: http://www.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/Simultaneous%20Categorization%20of%20Text%20Documents%20and%20Identification%20of%20Cluster-dependent%20Keywords.pdf
 [3]: http://www.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/ "http://www.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/"
