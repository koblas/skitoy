---
title: Language Design Choices
author: koblas
layout: post
date: 2011-07-12T12:45:00+00:00
url: /p/language-design-choices/383
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 8430
dsq_thread_id:
  - 356233888
categories:
  - General
tags:
  - python
  - ruby

---
Quick bit of background, I&#8217;ve used many programming languages over the years.  Though in general I would bias myself to being a procedural/object guy rather than a functional programmer.   Though I can say that I&#8217;ve done big projects in most of the popular languages at this point [C++, Java, JavaScript, Perl, PHP, Python, Ruby].   So, this post is more for trying to formalize a few of my thoughts, about some of what I&#8217;ve been working with/on.

One of the interesting things about languages is why they were created and then how did they evolve.  I might hold up awk as one of the first unixy interpreted languages, but I would sooner hold up Perl since it came from the open source world (you didn&#8217;t expect that AT&T was going to change awk, but Larry would change perl).  While we can look at perl and many people would happily talk about what is wrong with the language, myself included, fundamentally it was a great tool&#8230;  Most people forget that most of the original CGI programs on websites were written in perl &#8211; it got text in a way that no other tool did at the time (and most still dont).

I got into a discussion about how Ruby sucks, but realized later that this fundamentally was an origin problem.

### Author Centered &#8211;

I keep on making lots of comparisons between Ruby and Perl, maybe it all started because they both have &#8220;unless&#8221; as a keyword.  But, in thinking about it deeper most of the idea is that Perl has a single parent Larry and Ruby is Matz, the majority of the design of the language came from their world view.  The challenge is that most people have a strong understanding of a specific problem set, but they miss other details due to lack of understanding.  In perl, the OO and Variable hiding (my vs. local) I think demonstrates this, while in Ruby &#8220;returning from lambda&#8221; and extending base classes show it in other ways.

_Ruby Detail_:  If you extend Hash with a &#8220;fizzle&#8221; method, the challenge is that in a large project you import 57 gems one of which implements a &#8220;fizzle&#8221; method and the programmer before you used it&#8230;  You now have to figure out which gem extended your Hash class and what does the fizzle method do&#8230;  Pretty much impossible.

### Contribution Centered &#8211;

Just have to find a way to slip PHP in here.  It&#8217;s a kitchen sink, some of the language has OO style, some has procedural, sometimes the names change based on the phase of the  moon (look at the string functions).  It&#8217;s very clearly an open project where contributions are the primary driver, rather than strong design.

### Committee Centered &#8211;

Python, Java, JavaScript, C++ all of these have a strong committee  driving the design of the language, some are more old school some are more new school (C++ vs. Python).  But, what&#8217;s interesting is that proposals for the language end up being consistent with the existing style (vs. PHP) and tend to have lots of world views taken into account.  There feels like a correctness to the idea that False/0/empty string/empty array are all &#8220;false&#8221;.

In the grand scheme of things they are all tools, they all get a job done, it&#8217;s just working through the nuances of the langues takes time.  What&#8217;s interesting is that if you spend time to really work with these you will learn something new about all of the others that you will work with now and into the future, but sometimes it&#8217;s helpful to have a framework to put the underlying design into.

### A Few Final Thoughts &#8211;

  * Python &#8211; whitespace is great, but it makes adding/removing nesting hard.
  * Perl &#8211; You still rock for crunching a file quickly.
  * PHP &#8211; Visual Basic&#8230;  the early years.
  * Ruby &#8211; You&#8217;ve got more limits than you&#8217;ll admit to.
  * C &#8211; When you&#8217;re good, you&#8217;re great, when you&#8217;re not &#8230;. run.
  * C++ &#8211; Still teaching us tricks, separating the men from the boys.
  * Java &#8211; High hopes, not fulfilled.
  * JavaScript &#8211; Your second coming (nodejs) has promise
  * ActionScript &#8211; Why?
