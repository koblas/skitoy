---
title: Frameworks and sessions
author: koblas
layout: post
date: 2009-02-24T01:32:53+00:00
url: /p/frameworks-and-sessions/220
aktt_tweeted:
  - 1
pvc_views:
  - 2807
dsq_thread_id:
  - 689749129
categories:
  - Development
tags:
  - django
  - frameworks
  - zend

---
I hate sessions, they&#8217;re evil.

PHP is the worst offender since it&#8217;s built into the language and you end up with effective scalability limitations and turds in your temp file system. django isn&#8217;t much better since all of the cool admin functionality is built using the contrib.auth module which depends on sessions as well. Long ago in a galaxy far away I learned that such assumptions are bad, you should handle your authentication with some cookies that are totally independent of your application. Your sessions state should be passed around via posts or other URL tricks&#8230;

Don&#8217;t get me started today on the detail that django requires a &#8220;username&#8221; to authenticate. Half tempted to write the &#8220;uber auth&#8221; module which allows for both email registration and facebook/google connect, etc. authentication.
