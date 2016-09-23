---
title: Django performance
author: koblas
layout: post
date: 2009-04-23T18:15:28+00:00
url: /p/django-performance/228
aktt_tweeted:
  - 1
pvc_views:
  - 5387
dsq_thread_id:
  - 166941338
categories:
  - Development
tags:
  - django

---
I&#8217;ve been working on [I&#8217;ve been working on][1] and still having the love hate with python and django.  Areas that I would like see improved:

**Template Variables** : I&#8217;m currently doing strange things like:

```html
<body id="{% block tmpl_id %}{% endblock %}" class="{% block tmpl_class %}{% endblock %}">
```

and then the included template is setting those variables.  Which when you think about it is a bit off..

**Footer Scripts:** I would like to be able to stuff all the scripts in the footer, but there&#8217;s no easy way to faciliate &#8220;block append&#8221;  where any included template could include a short snippet to be appended to the footerscript block.

**Template Performance:** Ok, it&#8217;s good.  It really helped when I found a script to cache the parsed version of a template for rendering.  My page render time for most pages is < 100ms, which when you consider it&#8217;s running on a 5 year old machine.

**Models:** The models are a slippery slope, I&#8217;m finding that 90% of my functionality is drifting into the model layer, which is good&#8230; but, I don&#8217;t feel like there&#8217;s good seperation.

**File Layouts:** This really is django&#8217;s strongest and weakest point, it wants everything to be modular, but almost takes it too far for an application.  What&#8217;s an app whats a webapp?

**Auth:** django.contrib.auth _sucks_!  It forces two paradimes that should be abolished&#8230; SESSIONS and USER=AUTHENTICATION.   Long ago I learned that to use a SESSION object is a flawed approach, you should cache the database objects and reconstruct state as necessary, not depend on having things like a shoppping cart in memory.   The second bit is that if I want to provide multiple authentications system email+password, user+password, OAuth, Facebook having your user object tied to authentication is a bad practice.   The biggest problem is that I don&#8217;t want to re-write all of auth yet&#8230;

_That&#8217;s it today&#8230;more ranting later when&#8230;  Check out my [I&#8217;ve been working on [I&#8217;ve been working on][1] and still having the love hate with python and django.  Areas that I would like see improved:

**Template Variables** : I&#8217;m currently doing strange things like:

```html
<body id="{% block tmpl_id %}{% endblock %}" class="{% block tmpl_class %}{% endblock %}">
```

and then the included template is setting those variables.  Which when you think about it is a bit off..

**Footer Scripts:** I would like to be able to stuff all the scripts in the footer, but there&#8217;s no easy way to faciliate &#8220;block append&#8221;  where any included template could include a short snippet to be appended to the footerscript block.

**Template Performance:** Ok, it&#8217;s good.  It really helped when I found a script to cache the parsed version of a template for rendering.  My page render time for most pages is < 100ms, which when you consider it&#8217;s running on a 5 year old machine.

**Models:** The models are a slippery slope, I&#8217;m finding that 90% of my functionality is drifting into the model layer, which is good&#8230; but, I don&#8217;t feel like there&#8217;s good seperation.

**File Layouts:** This really is django&#8217;s strongest and weakest point, it wants everything to be modular, but almost takes it too far for an application.  What&#8217;s an app whats a webapp?

**Auth:** django.contrib.auth _sucks_!  It forces two paradimes that should be abolished&#8230; SESSIONS and USER=AUTHENTICATION.   Long ago I learned that to use a SESSION object is a flawed approach, you should cache the database objects and reconstruct state as necessary, not depend on having things like a shoppping cart in memory.   The second bit is that if I want to provide multiple authentications system email+password, user+password, OAuth, Facebook having your user object tied to authentication is a bad practice.   The biggest problem is that I don&#8217;t want to re-write all of auth yet&#8230;

_That&#8217;s it today&#8230;more ranting later when&#8230;  Check out my][1] site and send me feedback&#8230; I just need one solid day of love and I think it&#8217;ll be done&#8230;_

 [1]: http://zapquiz.com/
