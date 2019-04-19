---
layout: post
title:  "Advanced Kubernetes GKE Ingress Tutorial"
date: 2018-12-22 10:42:12 +0200
categories:
  - Kubernetes
---

Recently I was trying to setup cert-manager in Kubernetes cluster running on GKE and I have read
through Ahmet Alp Balkan's [tutorial][gke-tutorial] using gke ingress, as well as Daz Wilkin's
[Kubernetes w/ Let’s Encrypt & Cloud DNS][k8s-letsencrypt]. Both of them were good, but in real
world sceanrio the configuration is usually a bit more complicated. Here are few issues I had to
solve before make it working.

# cert-manager couldn't find secrets
One issue I had was the ClusterIssuer couldn't find the secret to GCP CloudDNS service account.
The error in ingress logs looks something like:
```
Re-queuing item "" due to error processing: error getting clouddns service account: secret "" not found
```

Since I created the ClusterIssuer in namespace `default`, the secret should naturally be created
in the same namespace, right? Wrong! You have to create the secrets where `cert-manager`
deployment is. In my case I have deployed `cert-manager` in namespace `cert-manager` so that's
where the secret should be. Problem solved.

# Mix using other signed certificate with Let's encrypt certificate
Sometimes we need to add an existing certificate that is signed by another issuer 

TBD

[gke-tutorial]: https://github.com/ahmetb/gke-letsencrypt
[k8s-letsencrypt]: https://medium.com/google-cloud/kubernetes-w-lets-encrypt-cloud-dns-c888b2ff8c0e
