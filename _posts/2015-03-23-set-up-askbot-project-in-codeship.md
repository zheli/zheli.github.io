---
id: 298
title: Set up Askbot project in Codeship
date: 2015-03-23T21:34:22+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=298
permalink: /2015/set-up-askbot-project-in-codeship/
dsq_thread_id:
  - 3878324318
categories:
  - Django
---
[<img class="aligncenter wp-image-309" src="http://i0.wp.com/www.systemsthoughts.com/wp-content/uploads/2015/03/codeship.png?resize=520%2C248" alt="codeship" data-recalc-dims="1" />](http://i0.wp.com/www.systemsthoughts.com/wp-content/uploads/2015/03/codeship.png)

<span style="color: #ff0000;">Update:</span>

<span style="color: #ff0000;">Askbot just <a style="color: #ff0000;" href="https://github.com/ASKBOT/askbot-devel/commit/929cba67ae17fc5183001adf4f732e30c0b635da">upgraded</a> their Django-avatar version so we don&#8217;t have to compile PIL anymore.</span>

[Codeship](https://codeship.com) is a great tool for private continuous integration system. But setting up a project that uses Askbot can be a bit troublesome, <del>since we have to compile PIL to support avatar module</del> in [offerQA](http://offerqa.com). <del>Mainly because it is not possible to symblink /usr/include/freetype2 to /usr/include/freetype. But later I realized that pip also searches in ~/.virtualenv/include folder so things became much easier.</del> A local_setting file is also created specifically for Codeship database and Redis. Here is my setup commands:

<pre class="wp-code-highlight prettyprint">pip install -r requirements-dev.txt
pip install redis
# Use settings for CI
ln -s local_settings.ci local_settings.py
# Sync your DB for django projects
python manage.py syncdb --noinput
# Run migrations for your django project
python manage.py migrate --noinput
</pre>

And here is my test commands:

<pre class="wp-code-highlight prettyprint"># Running your Django tests
python manage.py test
</pre>

The local_settings.ci file:

<pre class="wp-code-highlight prettyprint"># -*- coding: utf-8 -*-
DATABASES = {
    &#039;default&#039;: {
        &#039;ENGINE&#039;: &#039;django.db.backends.sqlite3&#039;,
        &#039;NAME&#039;: &#039;default.db&#039;,
        &#039;USER&#039;: &#039;&#039;,
        &#039;PASSWORD&#039;: &#039;&#039;,
        &#039;HOST&#039;: &#039;&#039;,
        &#039;PORT&#039;: &#039;&#039;
    }
}
CACHES = {
    &#039;default&#039;: {
        &#039;BACKEND&#039;: &#039;django.core.cache.backends.locmem.LocMemCache&#039;,
        &#039;LOCATION&#039;: &#039;offerqa&#039;,
        &#039;CACHE_TIMEOUT&#039; : 60,
        &#039;KEY_PREFIX&#039;: &#039;askbot&#039;,
    }
}
</pre>