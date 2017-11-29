---
title: XSide Thoughts...
author: koblas
type: post
date: 2007-10-24T16:08:59+00:00
url: /p/xside-thoughts/98
pvc_views:
  - 1374
dsq_thread_id:
  - 184764117
categories:
  - Development
tags:
  - sql

---
My brain is driving me crazy with building a CMS... No, no ... not another CMS you say... The thought isn't to build another CMS that's just like all the other CMS' --- I think DocuWiki is currently a contender if I wanted to do that... But, here's the requirements as I think of them.

* Easy to build pages --- either WYSIWYG or Wiki (Creole markup) based.
* You can easily favorite pages
* Page heirarcy [breadcrumbs, and property inheritance] 
  * ACLs
  * Watch lists --- when a page is changed, notify me...
* Different page types [ templates ? ]
* The two concepts that I would like to "figure out" 
  * DUCK Typed pages --
    The page has a variety of interfaces, which may or may-not be implemented
  * Publish / Subscribe --
    A Page on edit will publish a set of notifications about attributes on the page, which observers can then take action on.

Some data structures... just for the record

```
CREATE TABLE IF NOT EXISTS page_tags (
   guid         bigint unsigned not null, -- nice unique identifier
   tag          varchar(200),		  -- public URL identifier

   UNIQUE INDEX (guid),
   PRIMARY KEY (tag)
) ENGINE=InnoDB CHARACTER SET utf8;

CREATE TABLE IF NOT EXISTS documents (
   guid        bigint unsigned not null,     -- unique identifier
   pguid       bigint unsigned DEFAULT null, -- parent object...
   type        varchar(200),		     -- content type
   body        text,			     -- the content

   version     int,			     -- wiki history
   latest      enum('Y', 'N') DEFAULT 'Y',   -- is this the latest version
   note	       tinytext,	             -- revision comment

   created_on  TIMESTAMP,
   created_by  bigint unsigned,	      	     -- user_id
 
   FOREIGN KEY (create_by) REFERENCES user(user_id) ON DELETE SET NULL,
   PRIMARY KEY docid
) ENGINE=InnoDB CHARACTER SET utf8;

CREATE TABLE IF NOT EXISTS document_meta (
   guid        bigint unsigned not null,   -- unique identifier

   mkey        varchar(200),
   mvalue      text,

   INDEX       (guid, mkey),
   FOREIGN KEY (guid) REFERENCES pages(guid) ON DELETE SET NULL,
) ENGINE=InnoDB CHARACTER SET utf8;

```

If I have that right...

Forgot to document the page <-> doc table. But the idea is that a page would be composed of multiple documents... [think attributes]

doc.type might be something like:

* text/html --- Need to have plain old HTML
* image/gif --- Images, duh!
* text/wiki-creole --- Oh, something that might invoke a formatter
* application/xside-acl --- ACLs, or other objects need to be attached somehow
