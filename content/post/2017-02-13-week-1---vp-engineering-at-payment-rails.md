---
title: Week 1 - VP Engineering at Payment Rails
author: koblas
type: post
date: 2017-02-03T13:14:04+00:00
url: /p/week-1---vp-engineering-at-payment-rails/635
categories:
  - Payment Rails

---

I've started a new gig as the VP Engineering at  [PaymentRails](https://paymentrails.com) and a new city (Montreal). I'm going to try my best to give you a flavor of my time and the challenges faced in the real world.

### Background

Payment Rails is working on backend payment processing, it's a early stage startup which already has some traction and a great team of engineers who have made some great progress on the product. Most of the team has been around 4 months or less, working on a codebase they inherited. It's NodeJS/Express on the server and React on the client, with an Admin panel in AngularJS -- this is a startup that was built by contractors.

I'm coming into this as a player/coach role for the team, since in addtion to being here only a short time many of these guys it's their first real job. I'm very happy that the codebase is in good shape with it's interesting moments. Here's a quick run down of what I've found.

Good:

* Good coding styles
* Using git (recently migrated from GitLab to Bitbucket)
* Some amount of testing for the API layer
* Great specifications on features

Ugly:

* The React app build process was painful (2 minute builds)
* Weird Vagrant configurations to get a test environment working
* Lots of configuration and code intertwined
* console.log(...) everywhere
* No CI processes
* Lack of process, how issues are prioritized

What's great is it's an environment which is looking for some leadership both for process, management and architecture. The joy and fun of player coach.

### Where to start

It would be interesting to sweep in and start changing things, I have always felt the best thing to do is to listen and learn what is up. So I started with working on getting a running development environment up and running. Seeing where the build works, where the documentation is and _isn't_. Then continuing to move through the application.

In the process you need to work with your team as a newbie ask questions to gain understanding, see how the individuals work and get to know them a little bit on a interpersonal basis. 

When I walked in, I wanted to get a handle on the API layer of the application since that's critical to the bussiness. Getting that layer running was straight forward, except for some local database issues. To test it you need the UI running, that's where all the fun started.

The end of the week ended with the following accomplishments (technical):

* The frontend no longer takes 2 minutes to complie, it's down to 2 seconds
* There is automated builds and testing of the UI layer, short a lot of tests

Next week, it's off to people and process

* Getting gitflow style checkins
* Locking the master branch
* Pull requests and code reviews

Along the way, look at automating the API build process.
 


