---
title: Punctuation in Language Design is Good
author: koblas
layout: post
date: 2012-05-31T20:44:32+00:00
url: /p/punctuation-in-language-design-is-good/453
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 3638
dsq_thread_id:
  - 709998323
categories:
  - General

---
It&#8217;s all about CoffeeScript (and quietly about Ruby).

Why do people feel the need to remove punctuation?  I came across the following code snippet:

<pre>class TenFarms.View extends Backbone.View
  constructor: ->
    functions = _.difference _.functions(this), _.functions(TenFarms.View.prototype)
    _.bindAll.apply _, [this, "render"].concat(functions)
    super
</pre>

What I like and dislike &#8211; in line # order

  1. This is much better than the JavaScript equivalent &#8211; hands down.
  2. Nice, define a function.
  3. The beef
  
    GOOD &#8211; Sure you don&#8217;t need &#8220;var&#8221;
  
    BAD &#8211; Why no parens around \_.difference(\_.functions(this), &#8230;)
  4. Again, we&#8217;re depending on whitespace to cause things to happen.
  
    Think about this is: &#8220;A B&#8221; a function call?  What About &#8220;A B, C D&#8221; &#8211; did I forget a comma or is that two function call &#8220;A(B, C(D))&#8221;
  5.  &#8220;super&#8221; that&#8217;s good &#8211; better than the JavaScript version.

Bottom line, is when I&#8217;m reading Ruby or CoffeeScript I&#8217;m driven somewhat batty by when a function call happens.  All because they dropped the (&#8230;) requirement and now have some ambiguous cases.  Part of me has to wonder sometimes if the heavy emphasis on TDD is because of the adoption of such programming languages.