---
title: Cloud Databases are the Future
author: koblas
type: post
date: 2009-03-31T23:02:03+00:00
url: /p/cloud-databases-are-the-future/223
aktt_tweeted:
  - 1
pvc_views:
  - 3185
dsq_thread_id:
  - 160531972
categories:
  - Development
tags:
  - cloudb
  - couchdb
  - django

---
As I type this I&#8217;m sitting here watching MySQL shutdown after a bad up/down sequence and for the last five hours it&#8217;s been rebuiding it&#8217;s indexes&#8230; Fundamentally everything is down at this point, if it wasn&#8217;t for the backend services that are not tied to the database things would be ugly.

I&#8217;ve been preaching internally about cloud databases for the last few months and I&#8217;m totally convinced they&#8217;re the future. Why you ask? I only have a few requirements in my cloud database:

* Distributed and replicated store --
  I would like to make sure that I have N copies of any object and can support a read throughput of X across the store.

* Opaque object identifiers &#8212; within a &#8220;tablespace&#8221; --
  Every object should get a unique identifier on storage and the ability to reference it via a &#8220;key&#8221;, I don&#8217;t really care about  the ability to assign it.

* Indexable fields --
  This is where I can spec a primary key, I don&#8217;t want auto increment, since that&#8217;s just a crutch for uniquness&#8230; I&#8217;ve been happy to use things like:     base64.urlsafe_b64encode(uuid.uuid1().bytes).rstrip(&#8216;=&#8217;)

* Fast --
  Well duh, hopefully this is accomplished with the replication and the ability to tune the replication.

What can do this?  Or, where should I be spending my time evaluating technologies?

* CouchDB
* MongoDB
* Amazon S3
* Some custom Lucene + Storage mechanism
* Google Base
* _others?_

Though once that is complete, I need to have something like django support.  If you spend any time with django and Google App Engine you see that it works but half the power of django is missing since the nice folks at google ripped the model layer out.  It would be **really nice** if one could have the benifit of one of the above stores and build a whole django model layer out to support it&#8230;
