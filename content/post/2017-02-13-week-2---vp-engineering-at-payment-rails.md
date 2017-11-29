---
title: Week 2 - VP Engineering at Payment Rails
author: koblas
type: post
date: 2017-02-10T13:15:07+00:00
url: /p/week-2---vp-engineering-at-payment-rails/636
categories:
  - Payment Rails

---

# Week 2 - VP Engineering at Payment Rails


* CircleCI and API layer testing
* Understanding the DB schema
* External developers
* JIRA Process

This is the second in a series of blog posts / journal entries on my experiences as the new VPE at Payment Rails. 

## What happened this week

My original goal for this week as people and process, since last week was focused on getting a handle on code and release. Like many good intentionions, this didn't happen the way I wanted it to.

My final goal from last week was to take the build procecess (CircleCI) integrations that I had working at take them to the API layer. I expected this to be an "easy" process, since I already had the server running in Docker containers and there was already testing laying around. What I discovered was that the test environment had a lot more nuances to it than I expected and that it depended on running on an existing databases.

### The Ugly

The big "learning" for the team this week was that if you're building a unit testing harness, which is really an integration testing harness (depends on having a running DB, Redis and 3rd party API calls). You cannot insert a record with id = 1 and expect the DB with auto-increment keys to be happy with you. 

### The Good

* We've now gotten the whole team using GitFlow style branching, with Pull Requests and code reviews!
* Put together a presentation on React best practices after working on the Dashboard codebase for the week, team totally buys into having standards!
* Docker environments are fully running.

### Next week

* Process and people and finishing off the API server unit testing!
