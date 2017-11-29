---
title: Problem with Tomcat + WAR + ClassPath (help please)?
author: koblas
type: post
date: 2009-01-09T21:29:59+00:00
url: /p/problem-with-tomcat-war-classpath-help-please/214
aktt_tweeted:
  - 1
pvc_views:
  - 7808
dsq_thread_id:
  - 160531964
categories:
  - Development
tags:
  - java
  - tomcat

---
I've got a very simple problem... I'm trying to get a WAR file running under tomcat that references an external JAR file.

I thought it would be as simple as having a manifest file with a class-path. That doesn&#8217;t work, clearly I either need to set a web.xml context-param or enable tomcat to look at the manifest for the class path.

Help???
