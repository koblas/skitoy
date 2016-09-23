---
title: ES6 and Angular + a little GoLang
author: koblas
layout: post
date: 2015-07-08T19:00:44+00:00
url: /p/es6-and-angular-a-little-golang/588
pvc_views:
  - 1300
dsq_thread_id:
  - 3916432193
categories:
  - Development
tags:
  - golang
  - angular

---
This post really documents the checkpoint in my experiments with GoLang and Frontend development.  As some people might know that I&#8217;ve been playing around with application structure, languages and approaches for a while.

My [GoLang AngularJS and ES6 Todo App][1] over at GitHub &#8211; it&#8217;s the reference for the rest of this post.

### File Layout

Some quick to points, general directory structure:

```bash
go-angular-es6/
    - main.go    # Primary entry point
    - app/       # The GoLang application 
    - client/    # ES6 code libraries and html
      - app.html    # the main template
      - bootstrap/   # Bootstrap CSS
      - components/  # bower loaded components (JS Libraries)
      - partials/    # HTML fragments
      - app/         # ES6/Angular code
         - app.es6     #  Angular App - used for ES6 imports
         - main.es6    #  Main entry point
         - controllers #  Angular Controllers
         - services    #  Angular Services
    - conf/      # abstracted configuration
    - static/    # (not in GitHub) the output from building the client dir
```

One general note is that I haven&#8217;t found an idiomatic directory structure for GoLang application development.  IMHO &#8220;app&#8221; should be the handlers and have a model/conf directory.  Still a work in progress.

While this is an ES6 experiment, I did look at TypeScript for a bit and while I like it due to being a typed language which should reduce a class of errors. I did have to wonder about is the cost of building the type definition files for projects worthwhile?  In a large organization I could see that this would pay dividends, but not clear from the get go.

### What&#8217;s good about ES6

For past projects I&#8217;ve used CoffeeScript, since that is the standard which Tubular uses for projects and it&#8217;s always good to keep your mind working.  Plus as a Python/C programmer at heart I do find the CoffeeScript syntax where the parens are optional occasionally a bit hard to parse.

Top 3 likes of ES6

  1. classes
  2. import
  3. &#8220;=>&#8221; for functions

While it might be possible to go on, I haven&#8217;t had the chance to really fully exercise the language for my little ToDo app.  With the first two items the real need of CoffeeScript is diminished and allows you to program to the standard.

### General App Structure

This is where preference starts showing up.  How to structure a good AngularJS application.  I&#8217;m sure there is some conventions that I&#8217;m not following, either through ignorance or rebelliousness.  The biggest area where I think application standards are interesting is routing.

What I think is important is the ability to say in your main.es6 file:

```javascript
import './controllers/todo'
```

Then to have todo contain:

```javascript
app.config(($stateProvider) => {
    $stateProvider
        .state('app.todo', {
            url: '/todo',
            authenticate: true,
            views: {
                'content@app': {
                    template: require('../../partials/todo.html'),
                }
            }
        });
})

app.controller('TodoController', class TodoController {
   // ... more code here ...
})
```

This way you&#8217;re having the routing next to the controller, rather than having a massive route.es6 file which documents the whole application.

*Note:*  You&#8217;ll see that I also make use of browserify to load HTML into the controllers directly.  This makes it really easy to compress the whole application into a solid Single Page Application.

### Conclusion

I think ES6 is a good framework for building out AngularJS applications. The general problem is application structure, which is always a combination of personal preferences and habits.  That said, the Grunt flow with Babel and ES6 is easy to setup and make the code <em>much</em> cleaner.

 [1]: https://github.com/koblas/go-angular-es6
