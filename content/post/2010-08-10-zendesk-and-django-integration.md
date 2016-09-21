---
title: Zendesk and Django integration
author: koblas
layout: post
date: 2010-08-10T16:13:59+00:00
url: /p/zendesk-and-django-integration/283
pvc_views:
  - 4271
aktt_tweeted:
  - 1
dsq_thread_id:
  - 169673377
categories:
  - General

---
Part of this post is the gratuitous, gosh that was easy to integrate!  Of course part is a small point that I would like developers to think about.

First off here&#8217;s the code snippet, which owes it&#8217;s history to:

[Zendesk Remote Authentication with Django and Unicode Names][1] and [Zendesk remote authenticatin with Djnago][2] (the original posting)

<pre class="lang:default decode:true ">def authorize(request):
    if not request.user.is_active :
        return HttpResponseRedirect(reverse('openauth:signin'))

    try:
        timestamp = request.GET['timestamp']
    except KeyError:
        raise Http404

    u = request.user

    data = ''.join((u.profile.name(), u.email, u.username, settings.ZENDESK_TOKEN, timestamp))
    hash = md5(data.encode('UTF-8')).hexdigest()

    url = "%s/access/remote/?%s" % (settings.ZENDESK_URL, urllib.urlencode({
        'name' : u.profile.name(),
        'email' : u.email,
        'external_id' : u.username,
        'timestamp' : timestamp,
        'hash' : hash,
    }))

    return HttpResponseRedirect(url)
</pre>

&nbsp;

What&#8217;s different &#8212; or why am I making this post:

  * Use u.get\_full\_name() rather than the appends with the spaces, in my case I&#8217;ve got another object hanging out (profile) which contains the users name.
  * Use the django username as the external_id &#8212; I though about using user.id, but since username should be unique and fairly inflexible that&#8217;s a good approximation.
  * Use a join rather than a whole bunch of &#8220;%s%s%s%s&#8221; no formatting needed&#8230;

Finally, **the big rant** the original code used a bunch of formatted prints to build the URL argument.  If you&#8217;ve been handed a language with libraries like python and a framework like django, you don&#8217;t think about cross site scripting or other breakages (& in the username) which is going to cause problems&#8230;. It&#8217;s trivial to use urlencode to avoid these problems.

 [1]: http://bit.ly/bOP5zq
 [2]: http://bit.ly/c1Rkfu