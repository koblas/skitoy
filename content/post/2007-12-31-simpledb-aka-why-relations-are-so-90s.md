---
title: SimpleDB aka why Relations are so 90’s
author: koblas
layout: post
date: 2007-12-31T18:20:36+00:00
url: /p/simpledb-aka-why-relations-are-so-90s/126
pvc_views:
  - 2816
dsq_thread_id:
  - 186361180
categories:
  - General

---
I&#8217;m not really going to rant against relational databases, but this is more thinking about why technologies like CouchDB and SimpleDB are useful.

Some quick reference note:

* [Amazon SimpleDB and CouchDB compared][1]
* [Eventual Consistency Is Not That Scarry][2]
* [Falling Walls][3] &#8211; VC view

Many things can be said about databases but it&#8217;s the problem space that they are trying to tackle.&nbsp; If you look at applications like Wikipedia you have to wonder why you need a database to manage the content.&nbsp; Think about the objects that wikipedia manages:

* Page content
* User 
* Page permissions
* Edit history
* Inter page links
* &#8230; yes there&#8217;s a whole bunch more tables in MediaWiki &#8230;

Lets think about this for a second here, for account creation or other user oriented activites you need a transactional database to make sure your user objects are up to date &#8212; when you create an account you really want to have a single account created and active.&nbsp; When you edit a page, you personally want to see the edits but if it takes 10 minutes for the world to see the edit&#8217;s it&#8217;s probably not a big deal.&nbsp; Though of course if somebody else attempts to edit, you want to make sure they&#8217;ve got the edits out..

..put this down for two days&#8230; posting just to mark the links for posterity&#8230;

 [1]: http://www.automatthew.com/2007/12/amazon-simpledb-and-couchdb-compared.html
 [2]: http://smoothspan.wordpress.com/2007/12/22/eventual-consistency-is-not-that-scary/
 [3]: http://www.roughtype.com/archives/2007/12/falling_walls.php
