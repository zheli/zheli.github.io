---
id: 12
title: A simple SOAP mockup service in Python
date: 2011-05-31T12:37:16+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/index2.php/?p=12
permalink: /2011/a-simple-soap-mockup-service-in-python/
dsq_thread_id:
  - 3915335114
categories:
  - Automated Test
tags:
  - python
  - soap
  - test
---
I was dealing with SOAP tests a lot last month, and WireShark is little too much for simply checking a SOAP request. So I made a little script to show (not capture) the package content. It might be helpful if one needs automated SOAP testing as well. It&#8217;s very tiny (26 lines if use without Gzip) and doesn&#8217;t depend on any other modules.

Source code can be found at [https://bitbucket.org/zheli/soap\_echo\_server/](https://bitbucket.org/zheli/soap_echo_server/). Comments are welcome here:)