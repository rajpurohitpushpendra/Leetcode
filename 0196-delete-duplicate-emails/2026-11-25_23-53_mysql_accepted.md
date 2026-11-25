# 196. Delete Duplicate Emails
  
<br>**Problem:** https://leetcode.com/problems/delete-duplicate-emails/<br>

**Difficulty:** Easy<br>
**Topics:** Database<br>
**Language:** mysql<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-25 23:53 local time

**Runtime:** 840 ms (beats 70.82619999999982%)
**Memory:** 0 MB (beats 100%)


<!-- leetgit:submissionId=2203434792 codeHash=a2acd6e3ba6ead7724a9746fa325988797e09c4eadbb5c7023bfc6c656360006 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```mysql

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
WHERE p1.id > p2.id;

```
