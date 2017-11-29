---
title: HTTP status for API Responses
author: koblas
type: post
date: 2016-07-31T00:06:16+00:00
url: /p/api-design/622
pvc_views:
  - 176
categories:
  - Development
tags:
  - http
  - api

---
In designing an API it&#8217;s a challenge to understand when to use HTTP error responses and HTTP OK (200) responses. As with many organizations it&#8217;s something that can be subject to lots of passionate debate. Let&#8217;s look at a bunch of different scenarios.

Let&#8217;s take an OAuth 2.0 API that looks something like this, with an assumed HTTP Authentication header.

```
/api/v1/data.search?query=EXPRESSION&count=INTEGER
```

Imaging responses look something like:

```
{ ok: BOOLEAN, error: STRING, ... }
```

Where error is option if the ok boolean is False, otherwise there is a data payload appropriate to the API response.

#### data.search(query=&#8221;car&#8221;, count=15)

Return ok=true, code=200 and results=[array]

#### data.search(count=15)

Return ok=false, code=400, error=&#8221;query\_not\_found&#8221; – required parameter not present

#### data.search(query=&#8221;(car&#8221;, count=15)

Return ok=false code=200 error=&#8221;query_syntax&#8221; – there is a syntax error in the query

#### data.search(query=&#8221;car&#8221;, count=&#8221;xyz&#8221;)

Return ok=false code=200 error=&#8221;malformed_count&#8221; – count isn&#8217;t a number

### Shouldn&#8217;t errors be HTTP 400?

The discussion wouldn&#8217;t be so interesting if there was one answer to this. The objective is to differentiate between structural problems with your API requests and potentially customer generated syntax problem.

When you return a HTTP 400 level error you&#8217;re indicating a few key things:

  * Authentication errors
  * Rate limit errors
  * Non-existent endpoints
  * Missing mandatory parameters in requests

When you group syntax level events in here, it&#8217;s useful but what it means is when carried to an extreme you could have an autocomplete API endpoint that when there is no autocomplete results would return a HTTP 404 no results &#8212; that would be for a valid API query with valid parameters. When you&#8217;re doing an audit of your endpoints you cannot quickly determine if somebody is calling your API with missing parameters or it&#8217;s just normal events.

You could even argue in this model missing mandatory parameters are 200 &#8211; hold that thought.

Client Considerations

When a client dispatches a request what should it do with the error, let&#8217;s assume that you&#8217;re using a client that has request interceptors as part of the flow. Where if you were to call with a 401 Authentication error you would route the user to login in someway. This would be independent of the specific handler in your UI or application &#8211; similar if it&#8217;s server side the 429 rate limit would kick in and take an action above what your regular API was doing.

Now back to that syntax error, if you&#8217;re returning a 400 level event your interceptor logic is going to have to step in and try to understand why that problem happened and may or may not route back to the code that did the dispatch.

Now if you leave the 400 level HTTP errors to indicate that there was a problem with the call you can route all of these back to the code that dispatched and it can make local decisions for the right behavior is. It&#8217;s not an &#8220;error&#8221; for there to be no results to autocomplete, that&#8217;s normal expectations.

If you&#8217;re missing required parameters, you&#8217;ve got a serious bug in your code. That should be indicated in a way that&#8217;s distinct from normal failure.

### Recommendation

Given the idea that you want to have errors be programatic errors and ok&#8217;s be valid, this is what should be used for HTTP response code for APIs.

| HTTP Code | Description                                                                                |
| --------- | ------------------------------------------------------------------------------------------ |
| 200       | Structurally valid API request made &#8211; API &#8220;ok&#8221; boolean indicates details |
| 400       | No authentication provided or missing required parameter                                   |
| 401       | Invalid authentication token                                                               |
| 404       | Endpoint doesn&#8217;t exist                                                               |
| 429       | Rate limited                                                                               |
| 500       | Internal error &#8211; this should be returned even when a backend dies                    |
