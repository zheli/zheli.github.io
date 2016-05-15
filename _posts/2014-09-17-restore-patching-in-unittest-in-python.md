---
id: 268
title: Tips for mocking in Python
date: 2014-09-17T13:14:07+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=268
permalink: /2014/restore-patching-in-unittest-in-python/
dsq_thread_id:
  - 3932726773
categories:
  - Tips
---
## Restore patching

I like mocking and patching in unittest. And you shouldn&#8217;t forget to restore all the patchings also. I would think it should be put in the TearDown() method in a unittest. But it seems that I was wrong.

From the official document:

> &#8230;This method will **only** be called if the setUp() succeeds, regardless of the outcome of the test method&#8230;

So if there is an exception in setUp(), the patchings will not be restored. The correct way of doing it should be using the **addCleanup()** method.

> &#8230;If setUp() fails, meaning that tearDown() is not called, then any cleanup functions added will still be called.

And example if you use patch() as function.

<pre class="wp-code-highlight prettyprint">class MyTest(TestCase):
  def setUp(self):
    patcher = patch(&#039;package.module.Class&#039;)
    self.MockClass = patcher.start()
    self.addCleanup(patcher.stop)
</pre>

## Mock the base class

I am not sure if you should do that since I haven&#8217;t found too many articles on the internet. But I will put it here anyway. The base classes are defined in a class&#8217;s \_\_bases\_\_ attribute, but when I tried to patch it like other attribute using:

`@mock.patch.object(ExtendedClass, '__bases__', (MockBaseClass,))`

I got a TypeError:

`TypeError: can't delete ExtendedClass.__bases__`

Looks like mock module is trying to remove it before reassign it. I had struggled for a few hours before I found out another simple way to do it:

`ExtendedClass.__bases__ = (MockBaseClass,)`

The only drawback is that you will have to restore the base class manually afterwards.