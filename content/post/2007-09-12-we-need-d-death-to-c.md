---
title: 'We need ‘D’ {death to C++}'
author: koblas
type: post
date: 2007-09-12T15:31:43+00:00
url: /p/we-need-d-death-to-c/89
pvc_views:
  - 2686
dsq_thread_id:
  - 160530532
categories:
  - Development
tags:
  - languages

---
[Friend posted][1] a comment on a [rant by linus][2]

Ok, I admit it&#8230; I&#8217;m a C++ programmer&#8230; I don&#8217;t have an issue with STL, it&#8217;s pretty good&#8230; Why on earth would I want to re-implement a linked list? Sure, it&#8217;s got it&#8217;s pain, but so does every other _explitive deleted_ language.

But, Walter Bright had an [interesting comment][3] in this rant thread..

> Frankly, I don’t want to write loops that way. I want to write them like this:
>
> ```
>  void foo(int[] array)
>  {
>    foreach (value; array)
>    {
>       ... do something ...
>    }
> }
> ```

So, it&#8217;s time for a new language&#8230; How about D which is still a C, C++ lineage [no GC] but provides some of the functionality of &#8220;modern&#8221; type-smart languages (aka Java)

 [1]: http://brainwagon.org/?p=2539
 [2]: http://thread.gmane.org/gmane.comp.version-control.git/57643/focus=57918
 [3]: http://article.gmane.org/gmane.comp.version-control.git/58003
