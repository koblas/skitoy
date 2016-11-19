---
title: Using autoenv
author: koblas
layout: post
date: 2016-11-19T23:23:55+00:00
url: /p/using-autoenv/630
categories:
  - development

---

# Autoenv for greatness

This is really just a short post saying I discovered a really handy MacOS/Linux tool I hadn't seen before. [Autoenv](https://github.com/kennethreitz/autoenv) is a very handy tool for managing environments.

### Why would you need this?

If you've ever done any quantity of Python or Go work you're probably using [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) or [gvm](https://github.com/moovweb/gvm) to manage all of the different environemnts that you have. The challenge is that you want to quickly switch from one to the other when you enter that project workspace.

### Setup

Setting up autoenv is pretty easy -- you should read the docs, it's pretty much install the binary and add a line to your .bash_profile.

What happens is whenever you enter a directory (e.g. `cd`) the script will run anything in your `.env` file. For example:

Example .env file -- 

    gvm use go1.7
    gvm pkgset use snaplabs

That's it, now when I `cd` into that directory I've got my environment setup. I don't have to remember which go version I'm using and what packageset I'm using.

Script based configuration at it's finest.