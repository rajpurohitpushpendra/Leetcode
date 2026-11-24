# 175. Combine Two Tables
  
<br>**Problem:** https://leetcode.com/problems/combine-two-tables/<br>

**Difficulty:** Easy<br>
**Topics:** Database<br>
**Language:** mysql<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-24 20:13 local time

**Runtime:** 344 ms (beats 97.17409999999997%)
**Memory:** 0 MB (beats 100%)


<!-- leetgit:submissionId=2202647565 codeHash=95e20027663b3b6b4f532f36c8b5c80336e304c28cfed69869ea134311cf9aeb notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```mysql

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;

```
