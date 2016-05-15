---
id: 233
title: Some tips with Raspberry Pi development
date: 2013-11-16T14:56:57+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=233
permalink: /2013/some-tips-with-raspberry-pi-development/
categories:
  - Tips
---
### Change the permission for i2c

It is very annoying that you have to run your code with sudo to be able to use I2C. You can change it by doing this.

First add your user to i2c group:
  
`sudo adduser pi i2c`
  
then change the udev rules, here I changed rules for all the i2c devices. You have to edit 60-i2c-tools.rules file in your /lib/udev/rules.d/ folder.
  
`sudo nano /lib/udev/rules.d/60-i2c-tools.rules`
  
And change the following from
  
`KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"`
  
to
  
`KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0666"`
  
Save the file, type in the command below to reload udev rules.
  
`sudo udevadm control --reload-rules`