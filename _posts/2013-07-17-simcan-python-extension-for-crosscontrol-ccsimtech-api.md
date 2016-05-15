---
id: 205
title: SimCan Python extension for CrossControl CCSimTech API
date: 2013-07-17T17:25:40+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=205
permalink: /2013/simcan-python-extension-for-crosscontrol-ccsimtech-api/
dsq_thread_id:
  - 3922831625
categories:
  - New Project
---
Not sure if anyone needs this:)

Finally finished my first Python extension written in C language. It was a good practice. I have forgotten a lot about C, especially the pointers:) So use this library at your own risk!

The library is compiled in Visual Studio 2008 Express Edition so it only supports 32bit Python 2.7.x. It also doesn&#8217;t support unicode. Should be enough for CAN message I guess. Another important thing to know is I am not sure whether it works with CCSimTech non-developer license. I might test it later after summer.

This library implemented CanOpen, CanClose and CanReceive functions.

The file and document can be found [here](https://github.com/zheli/PySimCan).

&nbsp;