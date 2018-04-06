---
id: 30
title: Why you should never build your own test framework at work
date: 2011-07-09T12:54:43+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=30
permalink: /2011/why-you-should-never-build-your-own-test-framework-at-work/
categories:
  - Thoughts
tags:
  - experience
  - thoughts
---
Last week I moved parts of home-brewed automated test framework to [the robot framework](http://code.google.com/p/robotframework/). It went smoother than I thought and the new framework offered more functionalities that I was hoping to implement but didn’t for the sake of time. I wonder why I chose to write my own framework in the first place, since Robot framework came out few years ago. (probably because that test framework started as an experiment at work and was in “trial” ever since)

![Homebrew PC]({{ "/assets/images/homebrew_pc.jpg" | absolute_url }})

It reminds me a tip in <a href="http://pragprog.com/book/prj/ship-it" target="_blank">&#8220;Ship It! A Practical Guide to Successful Software Projects&#8221;</a>: using an “off the shelf” test framework. To most of the people (including me), it seems unnecessary in the beginning to learn to use a new framework just for a simple task. If I can finish it in a few lines of code, why bother spending days pick up something from start? But what people fail to see is automated test grows. A test suite will stay with the project forever and be executed after every change (that’s why you automated it, right?). As software changes, new functionalities need to be added. A few lines become hundreds or thousands lines of code. If you are lucky like me who created their own framework, you will find most of time you spend are not adding new test cases or data into the suite, but maintaining the framework. Since the framework runs as much as the test cases, or even more, there will be plenty of bugs and issues rising up to the surface. But this wouldn’t happen if you implement your tests with well-known test framework, since there are more people maintaining and it comes far more comprehensive from start.

What if there is currently no frameworks that fit your requirement? The best solution is to, still, choose a popular framework and start adding the missing function to it. There are possibly other people on the planet who would like to have the same function and will use or even improve it. So you spend the same amount of time implementing, but much less time maintaining. The employer should also support this because it saves resource and money.

The best example is Google chromium project. As a company famous of their re-inventing wheels, they are also adopting numbers of open-source tools and frameworks. In chromium they use buildbot for automated build and test instead of making their own framework. So next time think about if you can beat the whole chromium QA team before choosing your own framework over the “off the shelf” stuff:P
