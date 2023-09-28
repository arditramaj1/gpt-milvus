---
title: 'Add database index to vtiger_users.ename'
date: '2023-09-26T15:15:55.516Z'
tags: ['coreBOS', 'ToDo', 'coreBOS ToDo']
created: '2022-04-07T00:07:07.290Z'
creator: 'joe.bordes'
modifier: 'ardit.ramaj'
type: 'text/vnd.tiddlywiki'
bag: 'default'
assignedto: 'Mohamed'
difficulty: '1'
effort: '0.1'
priority: 'low'
project: ''
status: 'done'
tmap.id: '82dcdcfd-5d28-469c-965a-59d7c973b834'
revision: '3'
---

<!-- Exported from TiddlyWiki at 17:16, 26th September 2023 -->

# Add database index to vtiger_users.ename

```sql
ALTER TABLE vtiger_users ADD INDEX `idxename` (`ename`);
```

see if this makes a difference with explain. create changeset