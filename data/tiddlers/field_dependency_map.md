---
title: 'Field Dependency: Inititalize fields on duplicate'
date: '2023-07-27T08:04:31.436Z'
tags: ['cbQuestion', 'coreBOS', 'ToDo', 'coreBOS ToDo', '2do/Work']
assignedto: ''
created: '2023-07-26T09:44:35.070Z'
creator: 'joe.bordes'
difficulty: '3'
effort: '2'
modifier: 'joe.bordes'
priority: 'medium'
project: ''
status: ''
tmap.id: ''
type: 'text/vnd.tiddlywiki'
revision: '0'
bag: 'default'
---

<!-- Exported from TiddlyWiki at 17:05, 26th September 2023 -->

# Field Dependency: Inititalize fields on duplicate

this is implemented. not sure how but the Module2Module business map does this, so we DO NOT NEED TO IMPLEMENT THIS.

**Question**

> Where can I force fields to default when duplicating?

**Answer**

I don't think that is supported. From what I see in the code there is nothing doing that. Maybe we could try with a field dependency map but I don't remember there being anyway to indicate that we are in "duplicating" mode instead of creating mode.

I confirm there is no native way of knowing you are duplicating. There is a new input field in the form

`<input type="hidden" name="__cbisduplicatedfromrecordid" value="{$__cbisduplicatedfromrecordid}" />`

so the field dependency could execute a javascript function to look for that field and initialize some fields based on it's existence or not. In short, it is not possible to initialize field values when duplicating but it could be added using a field dependency custom function.

**Solution**

Use a "Field Mapping" (usign a special naming convention like `{modulename}_DuplicatingSetValues`) to define a javascript array of assignments that will be applied when duplicating. In other words, when entering "duplicate", in PHP we will search for a mapping with the values to be set, we transform those assignments into a javascript array that is sent to the browser. Then we add a `fieldDep_AssignValuesOnDuplicate` function that checks if the `__cbisduplicatedfromrecordid` input is present, if it is it uses the assignment array sent from PHP to initialize the fields.

Note, the existence of the mapping business map is not enough, they still have to create the field dependency map and call the `fieldDep_AssignValuesOnDuplicate` function