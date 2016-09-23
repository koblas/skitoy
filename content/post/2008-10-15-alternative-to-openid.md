---
title: Alternative to OpenID
author: koblas
layout: post
date: 2008-10-15T16:03:32+00:00
url: /p/alternative-to-openid/189
aktt_tweeted:
  - 1
pvc_views:
  - 7390
dsq_thread_id:
  - 160531952
categories:
  - Development
tags:
  - authentication
  - DNS
  - OpenID

---
I&#8217;ve never been a big fan of [OpenID][1], it feels like an interesting solution to a problem, but not the solution that makes sense.  For starters it requires me to learn something new, which as an &#8220;average&#8221; user I don&#8217;t want to do.

Quick education for those not familiar with OpenID.  OpenID allows you to have a single digital identity that enables you to log into multiple websites using one ID and password.  This means that when I find myself at a signin/signup form I can enter koblas.example.com (it could be as nasty as <span class="customoid">https://me.yahoo.com/a/nDvVG6521ORdniQiNkMGjNXR3g&#8211;</span>) as my identity.

From a practical standpoint it doesn&#8217;t make sense to have a second ID (or third, fourth, etc.) in the universe.  I&#8217;ve started &#8220;enjoying&#8221; websites which have given up on the USERNAME concept and just let me use an email address and password to signup/signin.   Now we&#8217;re drifting into an interesting world.

What I would like to see is my email address being my unique identifier, after all you&#8217;re going to send the account confirmation message there, I&#8217;m going to have to confirm it, etc. etc.  Product like [I&#8217;ve never been a big fan of [OpenID][1], it feels like an interesting solution to a problem, but not the solution that makes sense.  For starters it requires me to learn something new, which as an &#8220;average&#8221; user I don&#8217;t want to do.

Quick education for those not familiar with OpenID.  OpenID allows you to have a single digital identity that enables you to log into multiple websites using one ID and password.  This means that when I find myself at a signin/signup form I can enter koblas.example.com (it could be as nasty as <span class="customoid">https://me.yahoo.com/a/nDvVG6521ORdniQiNkMGjNXR3g&#8211;</span>) as my identity.

From a practical standpoint it doesn&#8217;t make sense to have a second ID (or third, fourth, etc.) in the universe.  I&#8217;ve started &#8220;enjoying&#8221; websites which have given up on the USERNAME concept and just let me use an email address and password to signup/signin.   Now we&#8217;re drifting into an interesting world.

What I would like to see is my email address being my unique identifier, after all you&#8217;re going to send the account confirmation message there, I&#8217;m going to have to confirm it, etc. etc.  Product like][2] are starting to show up and claim ownership of my identity.  Why not use email and DNS to take over for OpenID.

Here&#8217;s a proposed flow:

  * User is at the signin page
  * Enters koblas@example.com
  * DNS query is sent to lookup the &#8220;AUTH&#8221; record for &#8216;example.com&#8217;
  * result is authhost.example.com
  * Two choices at this point &#8211; either handshake ala OpenID or Facebook Connect &#8212; OR &#8212; have a DNS based auth lookup [the bias is to OpenID]
  * Now pop the user over to authhost.example.com with some arguments to authenticate
  * Return to mysite with cookies and tokens for their continued session.

Best part is that I don&#8217;t have to remember a new identifier, DNS handed out the identifier to complete the transaction.  You&#8217;re now going, but this will put the control of all identities into the hands of a few.  Sort of, but you can also think about it from the stance that if facebook were to have &#8220;public&#8221; email then you could use example@facebook.com as an identity for use on other sites.  They get the benefit that part of the authentication contract is that example@facebook.com is a deliverable email address to communicate with you at.

 [1]: http://openid.net/
 [2]: http://developers.facebook.com/news.php?blog=1&story=108
