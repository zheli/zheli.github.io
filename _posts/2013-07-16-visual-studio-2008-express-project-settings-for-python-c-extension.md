---
id: 198
title: Visual Studio 2008 Express Project Settings for Python C Extension
date: 2013-07-16T10:11:42+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=198
permalink: /2013/visual-studio-2008-express-project-settings-for-python-c-extension/
dsq_thread_id:
  - 4774011578
categories:
  - Tips
---
Here are some notes for setting up VS 2008 Express C++ project for Python extension development. For detailed information, you should check out [the official document](http://docs.python.org/2/extending/windows.html).

### Project type

Choose Visual C++->Win32->Win32 Project. The recommended project folder should be your Python source code folder.

### Application settings

In the application wizard, choose Application type: DLL. And check the box for &#8220;Empty project&#8221;.**
  
** 

### Project properties

[<img class="aligncenter size-medium wp-image-230" alt="configure_1" src="http://i2.wp.com/www.systemsthoughts.com/wp-content/uploads/2013/07/configure_1-300x209.png?fit=300%2C209" data-recalc-dims="1" />](http://i0.wp.com/www.systemsthoughts.com/wp-content/uploads/2013/07/configure_1.png)

First choose Configuration->All Configurations. In Configuration Properties->Linker->Command Line, add this into Additional options textbox:

`Here are some notes for setting up VS 2008 Express C++ project for Python extension development. For detailed information, you should check out [the official document](http://docs.python.org/2/extending/windows.html).

### Project type

Choose Visual C++->Win32->Win32 Project. The recommended project folder should be your Python source code folder.

### Application settings

In the application wizard, choose Application type: DLL. And check the box for &#8220;Empty project&#8221;.**
  
** 

### Project properties

[<img class="aligncenter size-medium wp-image-230" alt="configure_1" src="http://i2.wp.com/www.systemsthoughts.com/wp-content/uploads/2013/07/configure_1-300x209.png?fit=300%2C209" data-recalc-dims="1" />](http://i0.wp.com/www.systemsthoughts.com/wp-content/uploads/2013/07/configure_1.png)

First choose Configuration->All Configurations. In Configuration Properties->Linker->Command Line, add this into Additional options textbox:

` 

`(for example, if the function name is initspam, this line should be /export:initspam)`

Then choose Debug configuration. In Configuration Properties->C/C++->General, added the following two folder into Additional Include Directories (only if you created your project in the Python source code folder):

  * ..\..\Include
  * ..\..\PC

In Configuration Properties->Linker->General, change Output File to

<p style="padding-left: 30px;">
  $(OutDir)\$(ProjectName)_d.pyd
</p>

Additional Library Directories

<p style="padding-left: 30px;">
  ..\..\PCbuild
</p>

Finally, in Properties->Linker->Input, add Additional Dependencies

<p style="padding-left: 30px;">
  python27_d.lib
</p>

That&#8217;s it, you are done! Release configuration is almost the same just don&#8217;t forget to remove _d for output file and additional dependencies.