---
title: BackboneJS and RequireJS configuration
author: koblas
layout: post
date: 2012-06-18T23:05:51+00:00
url: /p/backbonejs-and-requirejs-in-configuration/455
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
pvc_views:
  - 7942
dsq_thread_id:
  - 731802869
categories:
  - General

---
One of the big challenges is getting backbonejs and requirejs working together without jumping through lots of hoops.  After reading quite a few blog posts, stackoverflow answers I finally came up with a simple canonical solution to the problem.

The assumed directory layout is something like:

```bash
static/
       app/
           config.js
           main.js
       vendor/
           ...third party stuff like backbone, jquery, etc.etc.
```

Cutting to the chase here&#8217;s the configuration file I use

```javascript
// This is your: static/app/config.js file
//
require.config({
    deps: ["main"],

    paths: {
        // Libraries
        jquery: "../vendor/jquery",
        underscore: "../vendor/underscore",
        backbone: "../vendor/backbone",
        handlebars: "../vendor/handlebars",
        bootstrap: "../vendor/bootstrap"
    },

    shim: {
        jquery: {
            exports: '$'
        },
        underscore: {
            exports: '_'
        },
        handlebars: {
            exports: 'Handlebars'
        },
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        }
    }
});
```

With that line in your HTML file and a configuration that is similar to what I've show you should be up and running, you can now create your main.js file that has the following simple format that you'll be extending shortly.

```javascript
// This is your: static/app/main.js file
//   - this is loaded as the deps: ["main"] in  your configuration
require([
  // Libs
  "jquery",
  "underscore",
  "backbone",
],

function ($, _, Backbone) {
});
```
