---
title: Using OpenID, OAuth, OAuth2 and OpenID+OAuth
author: koblas
layout: post
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
  - General
tags:
  - oauth
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

[code language=&#8221;py&#8221;]
  
class FoursquareOAuthClient(CommonOAuthClient):
      
api\_root\_url = &#8216;http://foursquare.com&#8217; #for testing &#8216;http://term.ie&#8217;
      
api\_root\_port = "80"

#set api urls
      
def request\_token\_url(self):
          
return self.api\_root\_url + &#8216;/oauth/request_token&#8217;
      
def authorize_url(self):
          
return self.api\_root\_url + &#8216;/oauth/authorize&#8217;
      
def access\_token\_url(self):
          
return self.api\_root\_url + &#8216;/oauth/access_token&#8217;

class FoursquareBackend(OAuthOpenBackend) :
      
name = &#8216;foursquare&#8217;
      
info = settings.OPENAUTH_DATA.get(name, {})

oauth_class = FoursquareOAuthClient

def get_profile(self, token) :
          
raw = self._fetch(token, &#8216;http://api.foursquare.com/v1/user.json&#8217;)

print raw

data = json.loads(raw)
          
data = data[&#8216;user&#8217;]

identity = &#8216;foursquare:%s&#8217; % data[&#8216;id&#8217;]

return identity, {
                          
&#8216;first_name&#8217; : data.get(&#8216;firstname&#8217;,&#8221;),
                          
&#8216;last_name&#8217; : data.get(&#8216;lastname&#8217;,&#8221;),
                          
&#8217;email&#8217; : data.get(&#8217;email&#8217;,&#8221;),
                      
}, data
  
[/code]

**OAuth2 &#8212;** The nice part is that it quick and easy to handshake up a token, but just like OAuth you still need an extra round trip.

[code language=&#8221;py&#8221;]
  
class GowallaBackend(OpenBackend) :
      
name = &#8216;gowalla&#8217;
      
info = settings.OPENAUTH_DATA.get(name, {})

def prompt(self) :
          
return &#8216;https://api.gowalla.com/api/oauth/new?%s&#8217; % urllib.urlencode({
                                  
&#8216;client_id&#8217; : self.key,
                                  
&#8216;redirect\_uri&#8217; : self.return\_to,
                          
})

def get\_access\_token(self) :
          
url = &#8216;https://api.gowalla.com/api/oauth/token&#8217;
          
body = {
                      
&#8216;client_id&#8217; : self.key,
                      
&#8216;client_secret&#8217; : self.secret,
                      
&#8216;redirect\_uri&#8217; : self.return\_to,
                      
&#8216;code&#8217; : self.request.GET[&#8216;code&#8217;],
                      
&#8216;grant\_type&#8217; : &#8216;authorization\_code&#8217;,
          
}

data = self._fetch(url, postdata=body, headers={&#8216;Accept&#8217;:&#8217;application/json&#8217;})

vals = json.loads(data)

return OpenToken(vals[&#8216;access_token&#8217;])

def get_profile(self, token) :
          
from ..libs.gowalla import Gowalla

go = Gowalla(self.key, access_token=token.token)

profile = go.user_me()

identity = "gowalla:%s" % profile[&#8216;url&#8217;]

return identity, {
                          
&#8216;first\_name&#8217; : profile[&#8216;first\_name&#8217;],
                          
&#8216;last\_name&#8217; : profile[&#8216;last\_name&#8217;],
                          
&#8217;email&#8217; : None,
                      
}, profile
  
[/code]

**OAuth+OpenID &#8212;** This is where life gets a bit more painful&#8230;  Typically over getting all of the URI bits worked out, where things go etc.  We won&#8217;t mention strange things like Yahoo doesn&#8217;t return the oauth token when asked unless you&#8217;ve approved yourself for non-public information&#8230;  Gack!

[code language=&#8221;py&#8221;]
  
class GoogleBackend(OpenBackend) :
      
name = &#8216;google&#8217;
      
info = settings.OPENAUTH_DATA.get(name,{})

def \_get\_client(self) :
          
client = consumer.Consumer(self.request.session, util.OpenIDStore())
          
client.setAssociationPreference([(&#8216;HMAC-SHA1&#8217;, &#8216;no-encryption&#8217;)])
          
return client

def prompt(self) :
          
client = self.\_get\_client()

auth_request = client.begin(&#8216;https://www.google.com/accounts/o8/id&#8217;)

auth\_request.addExtensionArg(&#8216;http://openid.net/srv/ax/1.0&#8217;, &#8216;mode&#8217;, &#8216;fetch\_request&#8217;)
          
auth_request.addExtensionArg(&#8216;http://openid.net/srv/ax/1.0&#8217;, &#8216;required&#8217;, &#8217;email,firstname,lastname&#8217;)
          
auth_request.addExtensionArg(&#8216;http://openid.net/srv/ax/1.0&#8217;, &#8216;type.email&#8217;, &#8216;http://schema.openid.net/contact/email&#8217;)
          
auth_request.addExtensionArg(&#8216;http://openid.net/srv/ax/1.0&#8217;, &#8216;type.firstname&#8217;, &#8216;http://axschema.org/namePerson/first&#8217;)
          
auth_request.addExtensionArg(&#8216;http://openid.net/srv/ax/1.0&#8217;, &#8216;type.lastname&#8217;, &#8216;http://axschema.org/namePerson/last&#8217;)

auth_request.addExtensionArg(&#8216;http://specs.openid.net/extensions/oauth/1.0&#8217;, &#8216;consumer&#8217;, self.key)
          
auth_request.addExtensionArg(&#8216;http://specs.openid.net/extensions/oauth/1.0&#8217;, &#8216;scope&#8217;, &#8216;http://www.google.com/m8/feeds&#8217;)

parts = list(urlparse.urlparse(self.return_to))
          
realm = urlparse.urlunparse(parts[0:2] + [&#8221;] * 4)

return auth\_request.redirectURL(realm, self.return\_to)

def get\_access\_token(self) :
          
if self.request.GET.get(&#8216;openid.mode&#8217;, None) == &#8216;cancel&#8217; or self.request.GET.get(&#8216;openid.mode&#8217;, None) != &#8216;id_res&#8217; :
              
raise OpenBackendDeclineException()

client = self.\_get\_client()
          
auth\_response = client.complete(self.request.GET, self.return\_to)

if isinstance(auth_response, consumer.FailureResponse) :
              
raise OpenBackendDeclineException("%s" % auth_response)

ax = auth_response.extensionResponse(&#8216;http://openid.net/srv/ax/1.0&#8217;, True)

self.email = ax.get(&#8216;value.email&#8217;,&#8221;)
          
self.first_name = ax.get(&#8216;value.firstname&#8217;,&#8221;)
          
self.last_name = ax.get(&#8216;value.lastname&#8217;,&#8221;)

self.identity = auth\_response.getSigned(openid.message.OPENID2\_NS, &#8216;identity&#8217;, None)

otoken = auth_response.extensionResponse(&#8216;http://specs.openid.net/extensions/oauth/1.0&#8217;, True)
          
oclient = GoogleOAuthClient(self.key, self.secret)

tok = oclient.get\_access\_token(otoken[&#8216;request_token&#8217;])
          
return OpenToken(tok[&#8216;oauth\_token&#8217;], tok[&#8216;oauth\_token_secret&#8217;])

def get_profile(self, token) :
          
v = {
              
&#8217;email&#8217; : self.email,
              
&#8216;first\_name&#8217; : self.first\_name,
              
&#8216;last\_name&#8217; : self.last\_name,
          
}
          
return self.identity, v, v
  
[/code]