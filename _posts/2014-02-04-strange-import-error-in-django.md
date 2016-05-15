---
id: 245
title: Strange import error in Django
date: 2014-02-04T13:15:45+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=245
permalink: /2014/strange-import-error-in-django/
categories:
  - Django
  - Tips
tags:
  - django
  - python
  - tip
---
Last night I started to have a string Import Error in my Django project in the development environment. It was working before and I haven&#8217;t changed any code yet.

## The Symptoms

I have a utils folder at the root of my django project with the following structure:

`Last night I started to have a string Import Error in my Django project in the development environment. It was working before and I haven&#8217;t changed any code yet.

## The Symptoms

I have a utils folder at the root of my django project with the following structure:

` 

And the problem appears in my code when I use:

`from utils import log as logging`

It gives me Import Error in some files but not all the files. Also if I use the shell I can load this module without problem. This whole thing is very strange. I checked the PYTHONPATH and PATH variable, but nothing seems to be wrong. So I created a new modules called libs with the same content and renamed the module name in all the code that complains import error.

## Solution

I decided to try to look into it again today to see if it can be fixed, but I couldn&#8217;t find anyone who has the same problem like me. Accidentally, I found an interesting comment:

> +1 just had similar problem to OP and removing *.pyc resolved it so thanks. this seems to work nicely`alias rmpyc="find . -name "*.pyc" -exec rm -rf {} \;"` to &#8216;clean&#8217; a project

And it worked! So it is because of the \*.pyc I got when I was working in other branches. I don&#8217;t know when Python will decide to recompile the \*.pyc file (or perhaps git removed the .py file, but left the .pyc file, and the code wasn&#8217;t cleaned up). But this is definitely something you need can try next time when you have an &#8220;Import Error&#8221;