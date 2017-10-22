---
id: 317
title: 5 things I learned using docker with bamboo
date: 2015-08-01T10:09:25+00:00
author: Zhe
layout: post
guid: https://www.systemsthoughts.com/2015/5-things-i-learned-using-docker-for-bamboo/
permalink: /2015/5-things-i-learned-using-docker-for-bamboo/
dsq_thread_id:
  - 3992448483
categories:
  - Tips
---
I decided to try out Docker for [Keycrunch](https://www.keycrunch.com) acceptance tests because the currently test setup with Bamboo is slow and complicated. To my surprise it was much simpler than I thought. The main tools I was using are Docker, Docker Machine (for Mac) and Docker Compose. And here are five things that I&#8217;ve learned.

### docker-compose up and docker-compose run is not the same

While you can start your service inside the docker by both commands, **`docker-compose run`** will not expose any ports. So to debug, I ended up adding a ssh service and then start the container with **`docker-compose up`**.

<span style="color: #ff0000;">Update: The document says you can use <code>--service-ports</code> flag for <strong><code>docker-compose run</code></strong> to create the ports, which I have just found out 😀</span>

### Use external-link to between system and acceptance test

Here is the docker-compose.yml file in the beginning (simplified version):

<pre class="wp-code-highlight prettyprint">web:
  build: .
  ports:
    - "80:80"
    - "443:443"
  links:
    - mysql
    - redis
mysql:
  image: mysql:5.5
  environment:
    MYSQL_ROOT_PASSWORD: docker
redis:
  image: redis:2.6
test:
  build: ../test-system
  links:
    - web
</pre>

One of the problems I have is that the part of the bootstrap process is in the entry script, and that takes some time to finish. So if I do

`docker-compose up test`

all the containers will start at the same time and test will be executed while web is still bootstrapping.

I solved it by using seperate docker-compose files and using external-link to connect them together. So for backend system:

<pre class="wp-code-highlight prettyprint">web:
  build: .
  ports:
    - "80:80"
    - "443:443"
  links:
    - mysql
    - redis
mysql:
  image: mysql:5.5
  environment:
    MYSQL_ROOT_PASSWORD: docker
redis:
  image: redis:2.6
</pre>

For test (backend is the project name for previous docker-compose project):

<pre class="wp-code-highlight prettyprint">test:
    build: .
    external_links:
        - backend_web_1:web
</pre>

Then you can easily just do it in two steps, first start backend

`docker-compose -p backend up -d`

And then do something to check if the bootstrap is finished, if it is run

`docker-compose -p qa up`

### Three other things

  * Dockerfile cannot read files in the parent folder, use volume or move your Dockerfile!
  * You will have to watch out for disk usage if the docker images are built on the fly (cleaning up old images constantly)
  * In Dockerfile, install your packages (pip install, npm install, etc) before copy all the files to minimize intermediate container images and make next build faster

&nbsp;
