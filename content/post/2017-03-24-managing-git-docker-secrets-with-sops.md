---
title: Managing Git Docker secrets with SOPS
author: koblas
layout: post
date: 2017-03-24T18:50:19+00:00
url: /p/managing-git-docker-secrets-with-sops/639
categories:
  - development
  - docker

---

# Managing Git/Docker secrets with SOPS

The classic problem in cloud engineering is that you have a bunch of API keys, secrets and passwords you need to have available to your code but not available to others. The ideal solution looks like:

1. You have your secrets in Git so you can merge them into config files
2. They're not availble to anybody who gets a copy of your repo
3. Your machines can easily decrypt them
4. You can edit them without a lot of work (e.g. reading a README everytime)
5. You would rather not setup a Hashicorp Vault environment (or any other server environment)

When I was at Tubular labs we had the classic problem which is somebody cloned a repo with our secrets and deleted a bunch of stuff but still put the repo up on GitHub for others to read... with all of that history. Nothing bad happened, but we did have a panic over the cleanup process - changing all the service keys in a 24 hour window is a pain.

Once again I'm faced with this challenge and spent a while digging around for a solution. After reading this gem of a blog post [Manage Kubernetes secrets with SOPS](https://frederic-hemberger.de/articles/manage-kubernetes-secrets-with-sops/) I was encouraged.

## Sources of information

For reference there are two good hacker news threads on the topic, both of which cover a lot of different tools that are useful.

* [	Biscuit: a multi-region key value store for your AWS infrastructure secrets](https://news.ycombinator.com/item?id=12112408)
* [Git-secret – store private data in a Git repo ](https://news.ycombinator.com/item?id=11662364)

I ended up doing a mental inventory of tools available, the above threads mention quite a few others. However there are only a few that look like they'll pass the first cut of "I trust this".

* [Hasicorp Vault](https://github.com/hashicorp/vault)
* [Amazon KMS](https://aws.amazon.com/kms/)
* [Shopify ejson](https://github.com/Shopify/ejson)
* [Stackexchange Blackbox](https://github.com/StackExchange/blackbox)
* [Mozilla SOPS](https://github.com/mozilla/sops)
* and many others...

Now the challenge is that I don't want to install Vault and operate a bunch of HA servers. We're a small startup and I'm playing SRE this mean that I've got about 10% of my time to be able to manage infrastructure, I want it to be as hands off as possible. Which means that Amazon KMS looks like the best solution since it's not something that I have to operate.

While researching around I really liked the idea of Shopify ejson, it was a very good solution which is to have JSON files in your repo that were encrypted. However since they operate in their own infrastructure the last mile isn't there, there is some brief talk about how their docker container load and init, but no demostration and clearly the key to decrypt is coming from somewhere.

## Digging into Amazon KMS 

Let's not and say we didn't. It's a key management service, that has more going on than I have brain cells to figure out.

## Why SOPS

KMS demonstrated that it takes too much work to figure out, but that's not a bad thing. What SOPS demonstrated is that it can use KMS to quickly deliver what I'm looking for.

1. The ability to edit JSON (or YAML,...) on my local machine quickly to add keys and then have them encrypted back into the file so it can be commited into Git.
2. The ability to have an AWS machine based on Role decrypt the secrets

### Quick guide

1. Setup KMS via your AWS console
2. Create a key with a useful alias
3. Install `sops`
3. Add it to your shell environment like so in your `.bashrc` (fyi this is random)

   ```
   export SOPS_KMS_ARN="arn:aws:kms:us-east-1:1234567890:key/48f5f29b-fd14-479a-baa1-cbf45b4ab39c"
   ```
     
4. Edit your secure json file:

   ```
   sops settings.sops.json
   ```
   
5. It's saved with all of your secrets encrypted.

#### Loading this at runtime

We're using nodejs on this project so loading is pretty easy:

```
let secure = {};
try {
  data = childProcess.execSync(`sops -d ${path.join(__dirname, "./conf/secure.enc.json")}`, { });
  secure = data ? JSON.parse(data.toString()) : {};
} catch (e) {
  console.error("Unable to decode secure data");
}
```

This is great since we never need to have decrypted data resident anywhere, it's loaded at runtime. If you can't load it (e.g. test environments, build machines) you don't have any KMS overhead.

