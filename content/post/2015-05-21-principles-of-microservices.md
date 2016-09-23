---
title: Principles of Microservices
author: koblas
layout: post
date: 2015-05-21T21:18:53+00:00
url: /p/principles-of-microservices/577
pvc_views:
  - 950
dsq_thread_id:
  - 3783572513
categories:
  - Development
tags:
  - architecture

---
Some principles that should be followed when designing micro services.

**Accuracy** – Fail hard or show full accurate results, never in between.

Our goal is to provide precise numbers customers trust. Sending incomplete numbers because our systems aren&#8217;t healthy can&#8217;t be an excuse, we should follow the rule of &#8220;all or nothing&#8221;.

**Scalability** – Predictable way to increase capacity.

Growing only the components that are over loaded. It&#8217;s easier to identify bottlenecks when it&#8217;s components that are fully instrumented and provide an accurate view of their performance.

**Simplicity** – Getting the whole picture and how our product is reflected in technology takes no more than one hour for anyone.

It&#8217;s important for new and existing team members to understand how system work and be able to jump into any area and figure out details as soon as possible.

**Speed** – Deliver as soon as we have new feature or bug fix.

Untestable code, long deployment cycles, high degree of dependencies or manual QA-ing are all blockers to make sure customers get fixes and features as soon as possible.  Small components with regression tests yield rapid deployment.

**Ownership** – Every component of the system is owned

Owner is the person who can answer any question about the service: current state, technical debt, development plan, core metrics, absolute numbers, issues etc.
