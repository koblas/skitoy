---
title: Set permission_required for your view functions
author: koblas
layout: post
date: 2008-09-22T19:05:25+00:00
url: /p/set-permission_required-for-your-view-functions/187
aktt_tweeted:
  - 1
pvc_views:
  - 4080
dsq_thread_id:
  - 194445046
categories:
  - General
tags:
  - django
  - python

---
Working with django 1.0 and google app engine&#8230; Wanted to set every view on my admin page to have admin permission.

<pre lang="python">def _perm_admin(rootfunc)  :
    import sys
    module = sys.modules.get(rootfunc.__module__)
    for key, value in module.__dict__.items() :
        if type(value) is types.FunctionType and key[0] != '_' and rootfunc.__module__ == value.__module__:
            module.__dict__[key] = permission_required('admin')(value)

_perm_admin(main)
</pre>