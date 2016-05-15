---
id: 252
title: Setup a remote development environment with Vagrant, Salt and Digitalocean
date: 2014-07-25T13:35:52+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=252
permalink: /2014/setup-a-remote-development-environment-using-vagrant-and-salt/
dsq_thread_id:
  - 3919471614
categories:
  - Tips
---
For years I have been doing web development on a lenovo S10 netbook via SSH. I like to be able to connect to it from anywhere in the world and resume my work by typing: `tmux -2u attach`. But it also has some issues:

  1. sometimes the connection is very slow in other countries because I have to SSH to my home router in Sweden.
  2. the laptop is getting older and the fan makes lots of noise.
  3. I cannot do system snapshot like a virtual machine.
  4. I cannot suspend/resume the system remotely like a virtual machine.

Since I have been using Vagrant and Salt for my web service, I figured I could setup a remote development environment using Salt. All of my repositories are at Github and Bitbucket anyway. As for the VPS,  I chose [DigitalOcean](https://www.digitalocean.com/?refcode=90161394e6ce) because of their API, price and speed:) Here is the github repository for my vagrant and salt files: <https://github.com/zheli/dev-environment>