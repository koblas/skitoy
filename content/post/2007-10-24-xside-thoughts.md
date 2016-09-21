---
title: XSide Thoughts…
author: koblas
layout: post
date: 2007-10-24T16:08:59+00:00
url: /p/xside-thoughts/98
pvc_views:
  - 1374
dsq_thread_id:
  - 184764117
categories:
  - General

---
My brain is driving me crazy with building a CMS&#8230;&nbsp; No, no &#8230; not another CMS you say..&nbsp; The thought isn&#8217;t to build another CMS that&#8217;s just like all the other CMS&#8217; &#8212; I think DocuWiki is currently a contender if I wanted to do that&#8230;&nbsp; But, here&#8217;s the requirements&nbsp; as I think of them.

  * Easy to build pages &#8212; either WYSIWYG or Wiki (Creole markup) based.
  * You can easily favorite pages
  * Page heirarcy [breadcrumbs, and property inheritance] 
      * ACLs
      * Watch lists &#8212; when a page is changed, notify me&#8230;
  * Different page types [ templates ? ]
  * The two concepts that I would like to "figure out" 
      * DUCK Typed pages
          
        The page has a variety of interfaces, which may or may-not be implemented
      * Publish / Subscribe
          
        A Page on edit will publish a set of notifications about attributes on the page, which observers can then take action on.

Some data structures&#8230; just for the record

<pre class="Code">CREATE TABLE IF NOT EXISTS page_tags (
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

</pre>

If I have that right&#8230;

&nbsp;

Forgot to document the page <-> doc table.&nbsp; But the idea is that a page would be composed of multiple documents&#8230;&nbsp; [think attributes]&nbsp;

doc.type might be something like:

  * text/html &#8212; Need to have plain old HTML
  * image/gif&nbsp; &#8212; Images, duh!
  * text/wiki-creole &#8212; Oh, something that might invoke a formatter
  * application/xside-acl&nbsp; &#8212; ACLs,&nbsp; or other objects need to be attached somehow

&nbsp;

&nbsp;