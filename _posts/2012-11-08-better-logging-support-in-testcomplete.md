---
id: 119
title: Better Logging Support in TestComplete
date: 2012-11-08T16:29:11+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=119
permalink: /2012/better-logging-support-in-testcomplete/
categories:
  - Automated Test
---
I have been using TestComplete since May. The test suite has been running since June. Not sure if I used TC in the right way. Now it just acts as a giant Java interpreter to execute all the code in JScript  (a fairly slow one in my opinion). I haven&#8217;t used too many of TC&#8217;s functions.

Anyway if you have to use script test case, you need to deal with logging. TestComplete offers four different levels: event, info, warning, error. Here is my code in my common_function.js file, which stores most of the generic functions:
  
[javascript toolbar=&#8221;true&#8221;]
  
function log_msg()
  
{
  
var msg = join\_log\_args(arguments);
  
Indicator.PushText(&#8220;[msg]: &#8221; + msg);
  
Log.Message(msg);
  
}

function log_event()
  
{
  
var msg = join\_log\_args(arguments);
  
Indicator.PushText(&#8220;[event]: &#8221; + msg);
  
Log.Event(msg);
  
}

function log_warn()
  
{
  
var msg = join\_log\_args(arguments);
  
Indicator.PushText(&#8220;[warn]: &#8221; + msg);
  
Log.Warning(msg);
  
}

function log_error()
  
{
  
var msg = join\_log\_args(arguments);
  
Indicator.PushText(&#8220;[error]: &#8221; + msg);
  
Log.Error(msg);
  
}

function log_debug()
  
{
    
if(vg_debug) //if debug is on
    
{
      
var msg = join\_log\_args(arguments);
      
var cl_priority = 200; //low priority
      
Indicator.PushText(&#8220;[debug]: &#8221; + msg);
      
Log.Message(msg, &#8220;&#8221;, cl_priority);
    
}
  
}

function join\_log\_args(args)
  
{
    
var log_string = &#8220;&#8221;;
    
for (var i=0; i < args.length; i++)
    
{
      
log\_string = log\_string + args[i] + &#8221; &#8220;;
    
}
    
return log_string;
  
}
  
[/javascript]
  
So if you want to log something, you just need to use:

<pre class="wp-code-highlight prettyprint">log_error(log_prefix, "this is an error, error code:", error_code);</pre>

and it will automatically join all the input parameters together.