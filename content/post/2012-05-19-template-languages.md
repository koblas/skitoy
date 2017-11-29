---
title: Template Languages
author: koblas
type: post
date: 2012-05-19T17:57:06+00:00
url: /p/template-languages/450
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 4358
dsq_thread_id:
  - 696476516
categories:
  - Development
tags:
  - html

---
Somehow I keep on building websites, re-building or otherwise&#8230;  Sometimes I think it just practice &#8211; just like playing a piano &#8211; most of the time it doesn&#8217;t have any true purpose, but it allows me to try different techniques and approaches.  When I think of big systems, NoSQL datastores (for example) it&#8217;s really hard to just play, it takes weeks to build the base system&#8230;   Then if you want to rebuild the IO subsystem it&#8217;s pretty involved, though I&#8217;ve  been know to do this&#8230;

Now back to templates!

I like the Zend Framework in PHP, it really helps abstract you from where the mess comes in (if you live in PHP).  However, it doesn&#8217;t relieve you of the worst risk in the language which is your templates are still in PHP.  One of the biggest points that drove me crazy at Yahoo! was their input filtering policy, where they mandated that some characters had to be removed from input to prevent people from accidentally letting them flow out to the HTML.   The challenge with this approach is that now all of a sudden you can&#8217;t have &#8220;&&#8221; or &#8220;<&#8221; in an input string&#8230;  You&#8217;re masking a class of bugs with a policy.

The following three lines are three different template systems for the same function:

```
<input id="name" name="nm" type="text" value="<?= htmlspecialchars($filter['nm']) ?/>" autocomplete="off" />
<input id="name" name="nm" type="text" value="{{ query.get('nm','') }}" autocomplete="off" />
<input id="name" name="nm" type="text" value="{{ query.nm }}" autocomplete="off" />
```

These are all real lines, two of which are in production &#8211; one is demonstration.

**Case #1** &#8211; You need to explicityly escape your code, thus meaning you mandate code reviews since bad things happen when people get tired of typing htmlspecialchars().  Which they do, because 30% of your code is &#8220;internal&#8221; safe variables &#8211; and you don&#8217;t need to escape&#8230;  But, of course you do &#8211; since the source data might have come in via an AJAX API that you implemented 6 months later&#8230;

**Case #2** &#8211; Good, escaping by default.  But, turns out that now you&#8217;re providing sensible defaults to everything.  But, typically the default is the empty string, failure to provide yields &#8220;None&#8221; or &#8220;null&#8221;.  More typing by rote, good but not great.

**Case #3** &#8211; I like this approach.  Two big value adds &#8211; Defaults are sensible, you don&#8217;t have to worry about the kind of data you&#8217;re dealing with.  Is it an object, is it a dictionary, is it an array ( result.location.3.title ) &#8211; is it a function&#8230;  By the time you get to the template level, you really just want as sensible default and an ERROR kicked into a logfile.  Don&#8217;t throw an error if result.location only has two items.

**Case #4** &#8211; Strange languages like HAML, at the end of the day HTML is the Lingua Franca between Engineering and Design&#8230; Why introduce translation.

At the end of the day, really think about how you&#8217;re abstracting things.  The goal of a good system  is the ability to get the maximum amount of work done with the minimum amount of syntax.  Since the more we type, the more mistakes happen, the more review is needed&#8230;

FYI &#8211; We&#8217;re looking at PHP, Tornado and Django (it could have been Handlebars).  Tornado makes no claims about being a full featured Template system, but until it get&#8217;s &#8220;big&#8221; it&#8217;s quick to whip things up in.  I really should wire up the 15 line Tornado<->Django connector that pulls Django templates into Tornado, but that&#8217;s another day.
