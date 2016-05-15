---
id: 143
title: 'Template tag &#8220;follow_all_url&#8221; failed to render unfollow links in django-activity-stream'
date: 2012-12-23T11:32:37+00:00
author: Zhe
layout: post
guid: http://www.systemsthoughts.com/?p=143
permalink: /2012/template-tag-follow_all_url-failed-to-render-unfollow-links-in-django-activity-stream/
dsq_thread_id:
  - 4375341429
categories:
  - Tips
---
I have been trying django-activity-stream for weeks now and it is a great Django app. Everything worked great until today, when the tag &#8220;**follow\_all\_url**&#8221; stops rendering unfollow urls.

I tracked back the problem back to a function in class **DisplayActivityFollowUrl** in **activity_tags**.py file:

[python toolbar=&#8221;true&#8221;]
  
def render(self, context):
      
actor_instance = self.actor.resolve(context)
      
content\_type = ContentType.objects.get\_for\_model(actor\_instance).pk
      
if Follow.objects.is\_following(context.get(&#8216;user&#8217;), actor\_instance):
          
return reverse(&#8216;actstream_unfollow&#8217;, kwargs={
              
&#8216;content\_type\_id&#8217;: content\_type, &#8216;object\_id&#8217;: actor_instance.pk})
      
if self.actor_only:
          
return reverse(&#8216;actstream_follow&#8217;, kwargs={
              
&#8216;content\_type\_id&#8217;: content\_type, &#8216;object\_id&#8217;: actor_instance.pk})
      
return reverse(&#8216;actstream\_follow\_all&#8217;, kwargs={
          
&#8216;content\_type\_id&#8217;: content\_type, &#8216;object\_id&#8217;: actor_instance.pk})
  
[/python]

**context.get(&#8216;user&#8217;)** is supposed to get the request.user, but instead it gets nothing. A <a href="http://stackoverflow.com/questions/4086076/how-to-get-request-user-in-a-templatetag" target="_blank">similar question</a> on stackflow indicates that a setting might be missing, which is not the case but I think it is something wrong with how I created the view. I use class-based generic view and here is how my **get\_context\_data**() looks like:

[python]
  
def get\_context\_data(self, **kwargs):
	  
ctx = kwargs
	  
ctx[&#8216;users&#8217;] = User.objects.all()
	  
return super(StreamView, self).get\_context\_data(**ctx)
  
[/python]

Doesn&#8217;t look like it is the problem:(

I remember at first I used activity-stream with **pinax-project-account** project, and it worked with **pinax-user-account** app which also does something with the context_processing setting. In this new project I remove the user-account app and switched it with **django-social-auth**, maybe it missed something in my context?

I haven&#8217;t found a solution yet, but I will post the update to the problem here. For now, I think I can temporarily change that line to **context.get(&#8216;request&#8217;).user** instead.

<font color="red"><br /> Update:<br /> It was quite stupid actually, I have an object list in the template called <strong>&#8220;users&#8221;</strong>, so in a for loop each iterated item is called <strong>&#8220;user&#8221;</strong>. Change that to <strong>&#8220;people&#8221;</strong> solved the problem.<br /> </font>