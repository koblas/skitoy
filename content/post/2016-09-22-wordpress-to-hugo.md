---
title: Wordpress to Hugo
author: koblas
type: post
date: 2016-09-22T13:28:07+00:00
url: /p/wordpress-to-hugo/635
categories:
  - General
tags:
  - wordpress
  - hugo

---

Upgrades might be the bane of modern life. Everything needs upgrades, reboots and changes. Sometimes it's under your control and sometimes it's not.

My linux box is reporting 948 days of uptime and still running version 3.7 of the kernel (4.4 is curently out). So it might be time for an upgrade, that's about 2 years and 7 months since the last upgrade. In the process I got to upgrade PHP and that's always fun to make sure all of the web servers, FPM modules and other things still continue to work. It's also the biggest security risk for my little linux box, which occasionally keeps me up when I find myself helping somebody de-virus another wordpress install (I've done that a few times, ugh). 

This blog was originally started back in 2004, where there wasn't a lot of choices and wordpress was a good choice and still is. But, one of the things that you need to be willing to do is "get smarter" not live with the choices you've made. So, some quick pros-cons of my decsission process.

A few of the core requirements --- 

* Static generation
* Support the existing URL scheme for postings
* Simple to install, maintain


&nbsp;                        | Wordpress | Jekyll | Hugo
------------------------|-----------|--------|---------
Community Size          | Large     | Medium | Small
Available Themes        | Large     | Medium | Small
UI for writing posts    | Yes       | No     | No
Secure site             | No        | Yes    | Yes
Upgrade frequency       | Frequent  | No     | No
Language                | PHP       | Ruby   | Go
Ease of install         | Hard      | Ok     | Easy

#### Wordpress

Choosing wordpress is like choosing IBM - it's the standard. The biggest challenge is that you need to keep on upgrading things to keep it "secure" and worry about every plugin you've ever installed. It has made me worry at times, though I've never had a problem over 12 years.

#### Jekyll 

This is probably the logical choice for most people, but after dealing with enough Ruby programs over the years, I do avoid Ruby when possible. Probably the second biggest community behind Wordpress for an Open Source blog platform.

#### Hugo

This is one of the "big 5" static blog platforms, Jekyll, GitBook, Hexo, Hugo, Octopress (based on GitHub stars), though all of the non-Jekyll ones occupy a stata that's pretty close.  


## Moving from Wordpress to Hugo - the dirt

You probably have already guessed that this blog moved from Wordpress to Hugo. So here's some details of what transpired behind the scenes.

1. Installation of Hugo
    -- pretty trivial, though I probably should have started on the Mac rather than my Linux box)
    
2. Selecting a Theme 
   -- this turns out to be hard, since the [Hugo theme selector](https://themes.gohugo.io/) is a great resource, it doesn't make as easy as Wordpress to preview themes.
   
3. Exporting content from Wordpress 
   -- the wordpress export utility works just fine.
   
4. Editing every blog post to "fix" the markdown 
   -- As it turns out, the export isn't perfect and you need to go back and fix a bunch of weirdness that creep into your posts... Everything from code formatting to weird HTML tables.
   
5. Iterate through themes 
   -- I test drove about 5 different themes before settling on Icarus, but even after choosing it there was a bunch of enhancements and bugs that needed some attention.
   * Search box doesn't work correctly with google
   * Supporting globally hiding the widgets
   * Overly agressive math formatting
   
6. Categories / Tags
   -- As of this writing, that's not done. When you read through everything you realize that you needed some more structure.
  
### Final Analysis

Hugo itself is great, had zero problems with running the core package. Everything from watching to serving to building, rocked. Where I spent all of my time was fixing HTML -> Markdown and fixing Theme bugs. The HTML->Markdown wouldn't have been fixable by any too, it was a known cost of the migration. What would be nice is to have a larger community of folks bulding themes for Hugo.

**Final Wish** A Editor GUI that has a "publish" button... I know I'm going to miss that from Wordpress, it's traded out for a pretty technical Git/Build flow (ah well, the cost of simplicity). 












