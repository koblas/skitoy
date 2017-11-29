---
title: Response to 10 reasons why I use PHP
author: koblas
type: post
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

Somebody is writing a book and cite these as the 10 reasons to use PHP, it's scary. Here's their 10 reasons, and my commentary.

  1. The PHP Community
  
      
    I'll agree that php.net set a new standard in language reference websites. The ability for users to comment on manual pages for functions is amazing. It turns a dry resource into something useful, code samples etc.etc. 
  2. Learning PHP is easy
  
      
    Basic is easy, Logo is easy... any interpreted language should be easy to learn. Since you are isolated from the system (no pointers to use, no memory to allocate). The other advantage that all modern interpreted languages share is good associative array constructs (thanks to Perl setting that standard). 
  3. It's Performance
  
      
    Ah.. no... While you can build an application that serves millions of pages a day on a server, when you really look at the performance of the language it sucks. You are still orders of magnitude from real performance. Not only that, but since PHP is designed around a single process model your ability to share data structures or connection pool resources is left to native code libraries. 
  4. The low cost
  
      
    Let's see... How many &#8220;0 cost&#8221; languages are there...</p> 
      * C 
      * C++ 
      * Perl 
      * Python 
      * Ruby [or else I'll get email] 
      * ...oh, all languages are zero cost... except for things like coldfusion 
  5. It's Open Source, You can modify it
  
      
    You can modify it if you need a hole in your head! Technically the point is that it's an open source project and they release patches often. You're point is that the community is actively working out the bugs. So, what any active language is doing this..</p> 
    Unfortunately C, C++ and Perl have all "died" at this point and will pretty much remain static at their current functionality.
    
  6. The built in libraries

      
    Java really is the library winner. PHP libraries are pretty sucky and are mainly written for PHP4, sure there's PEAR and PECL... But, getting any two libraries to interoperate is a pain since PHP doesn't really have #8. 

  7. Its Portability

      
    C is portable, it's just the OS bits that aren't. A lot PHP isn't portable to Windows since people don't use the OS abstractions to avoid some problems. 

  8. It has strong Object-oriented support

      
    Cough, Cough.. You've got to be kidding... The OO in PHP5 is better than nothing, but I wouldn't use the word "strong". Did you know that associative array's are 20% faster in PHP5 than using objects? There also isn't a **strong** set of base classes that can be used for abstractions. </p> 
    InputStream and OutputStream are great bases for any abstraction, it means that filters and other constructs can be layered and wrapped with no issue... Unless you build a whole class system from the ground up --- of course then you're the only user --- there's not a great OO approach to most problem.
    
  9. It has interfaces to a large variety of database systems

      
    True, but so does every other web programming language.. Perl had DBD/DBI before PHP was a twinkling in anybodies eye. 

  10. Support available
      
    Heck, there's support available for REXX --- both for $$ and free, but should you use that as a basis for greatness? </p>

   [1]: http://krillz.com/10-reasons-why-i-use-php/
