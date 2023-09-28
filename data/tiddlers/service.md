---
title: 'Service Worker update procedure'
date: '2023-09-19T13:10:20.413Z'
tags: ['coreBOS']
created: '2023-07-12T15:54:54.823Z'
creator: 'joe.bordes'
modifier: 'ardit.ramaj'
type: 'text/vnd.tiddlywiki'
revision: '0'
bag: 'default'
---

<!-- Exported from TiddlyWiki at 16:27, 20th September 2023 -->

# Service Worker update procedure

## Update coreBOS

* cd /var/www/coreBOSTest
* make sure to be on branch master, or checkout master if we are not
* git pull
* include/sw-precache/regen_swprecache
* git commit -m "cache(SW) update service worker cache" include/sw-precache/gitversion include/sw-precache/service-worker.md5 service-worker.js
* git push

## Update Evolutivo

* cd ../coreBOSNG/
* make sure to be on branch master, or checkout master if we are not
* git pull
* git pull corebos master
* git checkout –ours service-worker.js include/sw-precache/service-worker.md5 include/sw-precache/gitversion
* git add service-worker.js include/sw-precache/service-worker.md5 include/sw-precache/gitversion
* git commit
* include/sw-precache/regen_swprecache
* git commit -m "cache(SW) update service worker cache" include/sw-precache/gitversion include/sw-precache/service-worker.md5 service-worker.js
* git push