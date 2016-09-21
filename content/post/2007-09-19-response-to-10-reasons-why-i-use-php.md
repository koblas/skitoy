---
title: Response to 10 reasons why I use PHP
author: koblas
layout: post
date: 2007-09-19T16:00:57+00:00
url: /p/response-to-10-reasons-why-i-use-php/90
pvc_views:
  - 5042
dsq_thread_id:
  - 160530537
categories:
  - General

---
Read this article:
  
[10 reasons why I use PHP][1]

Somebody is writing a book and cite these as the 10 reasons to use PHP, it&#8217;s scary. Here&#8217;s their 10 reasons, and my commentary.

  1. The PHP Community
  
      
    I&#8217;ll agree that php.net set a new standard in language reference websites. The ability for users to comment on manual pages for functions is amazing. It turns a dry resource into something useful, code samples etc.etc. 
  2. Learning PHP is easy
  
      
    Basic is easy, Logo is easy&#8230; any interpreted language should be easy to learn. Since you are isolated from the system (no pointers to use, no memory to allocate). The other advantage that all modern interpreted languages share is good associative array constructs (thanks to Perl setting that standard). 
  3. It&#8217;s Performance
  
      
    Ah.. no&#8230; While you can build an application that serves millions of pages a day on a server, when you really look at the performance of the language it sucks. You are still orders of magnitude from real performance. Not only that, but since PHP is designed around a single process model your ability to share data structures or connection pool resources is left to native code libraries. 
  4. The low cost
  
      
    Let&#8217;s see&#8230; How many &#8220;0 cost&#8221; languages are there&#8230;</p> 
      * C 
      * C++ 
      * Perl 
      * Python 
      * Ruby [or else I&#8217;ll get email] 
      * &#8230;oh, all languages are zero cost&#8230; except for things like coldfusion 
  5. It&#8217;s Open Source, You can modify it
  
      
    You can modify it if you need a hole in your head! Technically the point is that it&#8217;s an open source project and they release patches often. You&#8217;re point is that the community is actively working out the bugs. So, what any active language is doing this..</p> 
    Unfortunately C, C++ and Perl have all &#8220;died&#8221; at this point and will pretty much remain static at their current functionality.
    
      * The built in libraries
  
          
        Java really is the library winner. PHP libraries are pretty sucky and are mainly written for PHP4, sure there&#8217;s PEAR and PECL&#8230; But, getting any two libraries to interoperate is a pain since PHP doesn&#8217;t really have #8. 
      * Its Portability
  
          
        C is portable, it&#8217;s just the OS bits that aren&#8217;t. A lot PHP isn&#8217;t portable to Windows since people don&#8217;t use the OS abstractions to avoid some problems. 
      * It has strong Object-oriented support
  
          
        Cough, Cough.. You&#8217;ve got to be kidding&#8230; The OO in PHP5 is better than nothing, but I wouldn&#8217;t use the word &#8220;strong&#8221;. Did you know that associative array&#8217;s are 20% faster in PHP5 than using objects? There also isn&#8217;t a **strong** set of base classes that can be used for abstractions. </p> 
        InputStream and OutputStream are great bases for any abstraction, it means that filters and other constructs can be layered and wrapped with no issue&#8230; Unless you build a whole class system from the ground up &#8212; of course then you&#8217;re the only user &#8212; there&#8217;s not a great OO approach to most problem.
        
          * It has interfaces to a large variety of database systems
  
              
            True, but so does every other web programming language.. Perl had DBD/DBI before PHP was a twinkling in anybodies eye. 
          * Support available
  
              
            Heck, there&#8217;s support available for REXX &#8212; both for $$ and free, but should you use that as a basis for greatness? </p>

 [1]: http://krillz.com/10-reasons-why-i-use-php/