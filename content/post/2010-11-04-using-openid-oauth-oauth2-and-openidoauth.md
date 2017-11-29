---
title: Using OpenID, OAuth, OAuth2 and OpenID+OAuth
author: koblas
type: post
date: 2010-11-04T18:14:16+00:00
url: /p/using-openid-oauth-oauth2-and-openidoauth/344
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 11965
dsq_thread_id:
  - 167177421
categories:
  - Development
tags:
  - oauth
  - python
  - OpenID

---
Over the last year I&#8217;ve had an authentication library that I&#8217;ve used to slice and dice public services and like most things it&#8217;s collected more than it&#8217;s share of dust, cruft and other ugly appendages that you wonder if it&#8217;ll work then next time you use it.  I&#8217;ve been hot and heavy over django (even if it&#8217;s embedded inside of Tornado) as a general framework for a while, it&#8217;s not broke don&#8217;t fix it&#8230;

The general case of site authentication looks like this:

  * You need your own username + password
  * You&#8217;re perfectly willing to give it all to Facebok/Google/etc. to handle

Depeding on the project I&#8217;m quite happy with giving it away, but there are times when you want to have &#8220;ownership&#8221; of the users on your website.  In which case in this day and age it&#8217;s important to allow people to associate their well known credentials with your service &#8212; cool.  FYI &#8211; This is my &#8220;new favorite flow&#8221;

  * Ask for email + password + (any service required fields &#8211; screen name &#8230;.)
  * Require them to associate with  another service 
      * Capture picture / full name and other bits from &#8220;Facebook&#8221;
  * Follow up with prompting to finish profile or other service specific tasks

That&#8217;s the simple part, the hard part has been dealing with OpenID, OAuth, OAuth2 and Hybrid protocols.   Since very rarely do you want just to get the fine photo for the user and forget about it.  You probably want to do one of these things:

  * Tweet something they did
  * Check in
  * Add to their facebook page
  * Scrape their friends
  * &#8230;etc&#8230;

Which means you need to store a token, not only that but some of these wonderful protocols don&#8217;t give you persistant identifiers.   Anyway, here&#8217;s a bit of commentary and some code excerpts for you to review, hopefully my refactorization makes life more interesting moving forward and those hulking if statements I used to have are gone.

**OAuth &#8212;** The big challenge is that the token you get is a transient identifier, it will change if you assocate account information with this your doomed.   So, typically what you end up needing to do is take your OAuth token and go back and pull the profile, which of course means that you need yet another round trip behind the scenes to get an authentication to happen.

```python

class GowallaBackend(OpenBackend) :
    name = ‘gowalla’
    info = settings.OPENAUTH_DATA.get(name, {})

    def prompt(self) :
        return ‘https://api.gowalla.com/api/oauth/new?%s’ % urllib.urlencode({
            ‘client_id’ : self.key,
            ‘redirect_uri’ : self.return_to,
        })

    def get_access_token(self) :
        url = ‘https://api.gowalla.com/api/oauth/token’
        body = {
            ‘client_id’ : self.key,
            ‘client_secret’ : self.secret,
            ‘redirect_uri’ : self.return_to,
            ‘code’ : self.request.GET[‘code’],
            ‘grant_type’ : ‘authorization_code’,
        }

        data = self._fetch(url, postdata=body, headers={‘Accept’:’application/json’})

        vals = json.loads(data)

        return OpenToken(vals[‘access_token’])

    def get_profile(self, token) :
        from ..libs.gowalla import Gowalla

        go = Gowalla(self.key, access_token=token.token)

        profile = go.user_me()

        identity = "gowalla:%s" % profile[‘url’]

        return identity, {
            ‘first_name’ : profile[‘first_name’],
            ‘last_name’ : profile[‘last_name’],
            ’email’ : None,
        }, profile

```

**OAuth+OpenID &#8212;** This is where life gets a bit more painful&#8230;  Typically over getting all of the URI bits worked out, where things go etc.  We won&#8217;t mention strange things like Yahoo doesn&#8217;t return the oauth token when asked unless you&#8217;ve approved yourself for non-public information&#8230;  Gack!

```python
class GoogleBackend(OpenBackend) :
    name = ‘google’
    info = settings.OPENAUTH_DATA.get(name,{})

    def _get_client(self) :
        client = consumer.Consumer(self.request.session, util.OpenIDStore())
        client.setAssociationPreference([(‘HMAC-SHA1’, ‘no-encryption’)])
        return client

    def prompt(self) :
        client = self._get_client()

        auth_request = client.begin(‘https://www.google.com/accounts/o8/id’)

        auth_request.addExtensionArg(‘http://openid.net/srv/ax/1.0’, ‘mode’, ‘fetch_request’)
        auth_request.addExtensionArg(‘http://openid.net/srv/ax/1.0’, ‘required’, ’email,firstname,lastname’)
        auth_request.addExtensionArg(‘http://openid.net/srv/ax/1.0’, ‘type.email’, ‘http://schema.openid.net/contact/email’)
        auth_request.addExtensionArg(‘http://openid.net/srv/ax/1.0’, ‘type.firstname’, ‘http://axschema.org/namePerson/first’)
        auth_request.addExtensionArg(‘http://openid.net/srv/ax/1.0’, ‘type.lastname’, ‘http://axschema.org/namePerson/last’)

        auth_request.addExtensionArg(‘http://specs.openid.net/extensions/oauth/1.0’, ‘consumer’, self.key)
        auth_request.addExtensionArg(‘http://specs.openid.net/extensions/oauth/1.0’, ‘scope’, ‘http://www.google.com/m8/feeds’)

        parts = list(urlparse.urlparse(self.return_to))
        realm = urlparse.urlunparse(parts[0:2] + [”] * 4)

        return auth_request.redirectURL(realm, self.return_to)

    def get_access_token(self) :
        if self.request.GET.get(‘openid.mode’, None) == ‘cancel’ or self.request.GET.get(‘openid.mode’, None) != ‘id_res’ :
            raise OpenBackendDeclineException()

        client = self._get_client()
        auth_response = client.complete(self.request.GET, self.return_to)

        if isinstance(auth_response, consumer.FailureResponse) :
            raise OpenBackendDeclineException("%s" % auth_response)

        ax = auth_response.extensionResponse(‘http://openid.net/srv/ax/1.0’, True)

        self.email = ax.get(‘value.email’,”)
        self.first_name = ax.get(‘value.firstname’,”)
        self.last_name = ax.get(‘value.lastname’,”)

        self.identity = auth_response.getSigned(openid.message.OPENID2_NS, ‘identity’, None)

        otoken = auth_response.extensionResponse(‘http://specs.openid.net/extensions/oauth/1.0’, True)
        oclient = GoogleOAuthClient(self.key, self.secret)

        tok = oclient.get_access_token(otoken[‘request_token’])
        return OpenToken(tok[‘oauth_token’], tok[‘oauth_token_secret’])

    def get_profile(self, token) :
        v = {
            ’email’ : self.email,
            ‘first_name’ : self.first_name,
            ‘last_name’ : self.last_name,
        }
        return self.identity, v, v
```
