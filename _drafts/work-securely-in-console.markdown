---
layout: post
title:  "4 Tips on working securely and safely with operation"
date: 2018-11-22 22:10:23 +0200
categories:
  - Tips
  - Security
---
At Minna we take security very seriously, since we are working with critical financial data. In this post I will share
some tips I used in my daily ops work.

# Manage Credentials Safely
It's important to use strong password, as well as not re-using passwords. The easiest way to do that is using a password
 manager.

Personally I would recommend [Lastpass][lastpass-ref]. There are many sources online regarding its design, with the most
 famous one being from [Steve Gibson][steve-gibson]. It's free to use on all devices, but I am paying for their premium
 plan because I just like the company:)

# Use the Right K8s Context
This is not an issue if you are riding the latest GitOps train and let CI/CD pipeline apply all the Kubernetes changes.
But if your are old-school like me :D, you will probably use `kubectl apply` a lot.

When you work with several Kubernetes (refer to as K8s below) clusters, there will be more than one kubectl config
context in your `~/.kube` folder. And at any given time there is also a default config context in the shell session.
It's very easy to apply a test K8s yaml file to a production environment if you are not careful. Here are few console
tools that may help you to avoid that.

#### kubectx
Github: <https://github.com/ahmetb/kubectx>
![kubectx](https://raw.githubusercontent.com/ahmetb/kubectx/master/img/kubectx-demo.gif)

I would say this is a MUST if you are working with K8s clusters. It just made it so easy to switch between K8s context
and namespaces. Honestly I don't know why kubectl didn't add a feature like this.

#### kube-ps1
Github: <https://github.com/jonmosco/kube-ps1>
![kube-ps1](https://raw.githubusercontent.com/jonmosco/kube-ps1/master/img/kube-ps1.gif)

This plugin will show the current K8s context and namespace in your shell prompt and it supports zsh out of box. I
removed it eventually because my prompt is just simply just too long. (git branch name, virtualenv...)

#### tmux-kube
![]({{"/assets/images/tmux-kube.png"|absolute_url}})
I am using this plugin from <https://github.com/sudermanjr/tmux-kube> show K8s context and namespace in my tmux status
bar. Unfortunately the original repository is no longer exists:( I will re-upload my local version to github one day.
But you should be able to find many alternatives on Github.

Here is the left status for my Tmux if you are interested.
```
set -g status-left '#[fg=colour232,bg=colour39,nobold] #S #[fg=colour39,bg=colour245,nobold]#[fg=colour233,bg=colour245] #(whoami) #[fg=colour245,bg=colour240] #I:#P #[fg=colour240,bg=colour235] k8s:#[fg=colour69,bg=colour235,nobold]#{kube_cluster}#[fg=colour240,bg=colour235]:#[fg=colour11,bg=colour235]#{kube_namespace} #[fg=colour235,bg=colour233,nobold]'
```

#### Always use "--context" parameter
This is one extreme

So to know
* TODO PS1 extension
* kctx
* always use context parameters

# Command Line History

# Final Thoughts
And finally, a system is only as secure as its weakest points. So don't forget to educate your colleagues :)

[lastpass-ref]: https://lastpass.com/f?6324856
[steve-gibson]: https://en.wikipedia.org/wiki/Steve_Gibson_(computer_programmer).
