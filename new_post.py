#!/usr/bin/env python

import os, time
#import readline

BASE_DIR = 'content/post/'

files = sorted([file for file in os.listdir(BASE_DIR) if file != '.'])

post_id = 0
with open(os.path.join(BASE_DIR, files[-1]), 'rb') as fd:
    for line in fd:
        if line.startswith('url:'):
            post_id = int(line.split('/')[-1])

if post_id == 0:
    print("Unable to find post_id")
    exit(1)

post_id = int(post_id) + 1

title = None
while not title:
    title = raw_input('Title for post: ')

slug = title.lower().replace(' ', '-')

template = '''---
title: %(title)s
author: koblas
layout: post
date: %(date)s
url: /p/%(slug)s/%(post_id)s
categories:
  - draft

---

# TEXT HERE
'''

tnow = time.gmtime()
tstr = time.strftime('%Y-%m-%dT%H:%M:%S+00:00', tnow)
output = os.path.join(BASE_DIR, '%s-%s.md' % (time.strftime('%Y-%m-%d', tnow), slug))
vars = { 'title': title, 'slug': slug, 'post_id': post_id, 'date': tstr }

if True:
    with open(output, 'wb') as fd:
        fd.write(template % vars)

    print "OUTPUT = ", output
else:
    for k, v in vars.items():
        print "%s = %s" % (k, v)
