---
id: 163
title: Setup Postgresql, Python2.7 and Django using virtualenv on CentOS 6.3
date: 2013-03-25T16:52:29+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=163
permalink: /2013/setup-postgresql-python2-7-and-django-using-virtualenv-on-centos-6-3/
dsq_thread_id:
  - 3962354736
categories:
  - Tips
---
Setup server is always a pain in the ass (if you don&#8217;t know [chef](http://www.opscode.com/chef/) or other similar tools). It took me two days to get my django app running on the VPS. My problem is there are a lot of tutorials on the website, but few of them cover everything. Also the tutorials are not always working for me, there are many weird problems that are very difficult to Google. So I made some notes for myself, hope it can help you as well.

### Postgresql 9.2 on CentOS 6.3

  * Order of entries in pg_hba.conf is important. Always add the new user to the top of the list (that means before host all all).
  * If localhost gives you ident error, try connect using -h 127.0.0.1. Might be your VPS is using ipv6 address for localhost.
  * initdb with UTF8 support when your database is still empty.

### Deploy Django using Apache + WSGI + Virtualenv

It seems simple from beginning because I have configured it with non-daemon mode before. This time I try to make it run in daemon mode. The tricky thing is there are many reasons for you to end up with a &#8220;ImportError: No module named django.core.wsgi&#8221; error. Here is a list you can go through to figure it out:

  * did you install mod\_wsgi.so using yum? The module in yum is only for Python 2.6 so you have to compile your own mod\_wsgi.so file.
  * run &#8220;ldd mod\_wsgi.so&#8221; to check if libpython.2.7.so.1 shows up. if not, you have to recompile python2.7 and mod\_wsgi with &#8211;enable-shared option.
  * if it still gets that error, check the permission setting for your virtualenv folder, is the user running daemon has enough privilege?