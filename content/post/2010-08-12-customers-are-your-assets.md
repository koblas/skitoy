---
title: Customers are your assets
author: koblas
type: post
date: 2010-08-12T16:13:25+00:00
url: /p/customers-are-your-assets/299
aktt_tweeted:
  - 1
pvc_views:
  - 2863
dsq_thread_id:
  - 423305730
categories:
  - Development
tags:
  - authentication
  - facebook connect
  - ltv
  - oauth

---
I&#8217;ve been wrangling with use registration for years, partly because it&#8217;s an interesting time sink.  Partly because it&#8217;s annoying when it&#8217;s wrong.  Plus, usually when you start building any application in this day and age you need some form of user registration.  The basic systems these days are:

  * Username and Password  (e.g. yahoo, google) 
      * Key signup form elements: Username, Email, Password, Captcha
  * Email address and Password (e.g. facebook, linkedin) 
      * Key signup form elements: Email, Password, Capthca
  * Pure Facebook Connect (or Google Connect, etc.) 
      * Key signup form elements: Big Facebook button
  * Hybrid systems 
      * ..topic of discussion&#8230;

Fundamentally username+password and email+password are just variants of themselves, really coming down to how you are known on the system (unique handle &#8220;johndoe77&#8221; vs. real name &#8220;John Doe&#8221;).  Both systems typically will send you and email asking you to confirm your email and they always have a Captcha since the spammers are going to bully you into submission if you don&#8217;t. **It&#8217;s really hard to innoviate in this space** it&#8217;s just getting the implementation right, but I&#8217;ve build four or fourty of these in the past.

The new kid on the block is the Facebook Connent, Google Connect, OAuth/OpenID systems.  The happy part is that as sites start implementing these systems we can stop having to type our passwords into site after site after site &#8212; do you really make unique passwords?!?.   The challenge is that as a service you still want to have connection with your user.  Things I&#8217;ve noticed:

  * Google gives you email address _easily_ (thanks guys)
  * Facebook gives you a handle to email address and prompts for permission (so, so)
  * LinkedIn you&#8217;re just a pain in this front, I want a relationship with your user, not just some handle to use your funked up messaging platform.
  * Twitter/Yahoo &#8211; data exchange is a pain.

Back to owning our user!  It&#8217;s easy to own the user if they type a password, it gets progressively harder when we start using the Open provider marketplace to have the user.

**Why should you care?** Because users are your biggest asset!  If you don&#8217;t realize that you&#8217;re not thinking hard enough.  The cost of customer acquisition is $X in this day and age the cost of marketing to a known user is a fraction of $X (say 1/10th).  Which means that if you have a service and spent $100 on Google ad words to find customers the cost to market a new product to them is $10 rather than $100 &#8212; plus you don&#8217;t have to re-train them hopefully so your support costs are lower.

That brings me to my last world view of customer registration &#8212; hybrid registration.  No I don&#8217;t have a quick example deployed at the moment (currently in alpha).  The basic premise is that you ask for the basics up front:

  * Username
  * Password
  * Email address

But now instead of the classic &#8220;captcha&#8221; page you hit them with the Facebook Connect/Google Auth page to confirm their account.  The complexity of getting this working is slightly higher than the Captcha, but the advantage is that in addtion to having about the same barrier as a Captcha from a spam protection standpoint you also now have a secondary form of authentication and potentially access to very useful data about your customer.

  * Friends/Contacts
  * Full Name
  * &#8230;etc&#8230;

While you&#8217;re probably a smart service and don&#8217;t hit the customer over the head with &#8220;spam your friends&#8221; what you can do is save this away for later use, like when &#8220;Sally Smith&#8221; joins you notice that &#8220;Tom Jones&#8221; is a friend of hers and you can point this out in &#8220;Suggested Friends&#8221;.  Sally just thinks that you&#8217;re a smart service &#8212; maybe goes &#8220;how did they know that&#8221; &#8212; but you&#8217;re really  using the information for their own good.

The second benifit is that since you&#8217;re still running a user through a classic registration flow, you&#8217;ve got an email address to conduct future marketing to.   But not just that you&#8217;ve also now got a guaranteed second touch with the customer.  Why&#8217;s that important?

  * Your **first touch** was getting them to signup and confirm their account, because they connected a social network to their account we&#8217;ve got a high confidence that it&#8217;s a real user.
  * Your **second touch** is the confirmation email, which the user will now open 30 minutes to a day later.  Where you can remind them of all the cool things they should be doing with your service.
  * Your **third touch** is the message you send in three to seven days thanking them for signing up for your service and potentially looking at some of their recent behaviors on the site to determine some simple bucketing of their behavior to help send an appropriate message.

If you feel like I jumped from Hybrid authentication to customer contact, you&#8217;re right.  But, fundamentally as I&#8217;ve played with user authentication and buit a variety of systems and looked at the long term value of that customer.  My mindset has evolved into these tenets:

  * Own your user &#8212; don&#8217;t give them away
  * Enable them to login with a variety of system &#8212; lower the barriers
  * Keep the lifetime value of your user in mind

Hybrid authentication is the way to go!
