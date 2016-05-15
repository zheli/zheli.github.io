---
id: 281
title: No Django log printout in Gunicorn
date: 2014-10-19T21:17:55+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=281
permalink: /2014/no-django-log-printout-in-gunicorn/
dsq_thread_id:
  - 3893122531
categories:
  - Django
  - Tips
---
I found a weird problem when I tried to deploy a new project with Gunicorn this weekend. It seems Gunicorn has swallowed all Django printouts. No matter how I set up the project: change the logging settings in Django, add debug flag and set log level, I couldn&#8217;t get anything to show up.

After a couple of hours of trying and googling (!!!) I found an interesting comment in Stackoverflow, it seems Gunicorn has changed the default logging to not to print on the console in R19, but it is reverted back in R20. But if you are using R19, you can get Gunicorn to write log to console again by adding:

> `--log-file=-`

flag to the command.