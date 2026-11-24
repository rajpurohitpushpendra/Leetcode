# 181. Employees Earning More Than Their Managers
  
<br>**Problem:** https://leetcode.com/problems/employees-earning-more-than-their-managers/<br>

**Difficulty:** Easy<br>
**Topics:** Database<br>
**Language:** mysql<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-24 20:24 local time

**Runtime:** 302 ms (beats 99.4209%)
**Memory:** 0 MB (beats 100%)


<!-- leetgit:submissionId=2202653755 codeHash=f38ed6394175d18bc9233744455e5bf8118fb0638a2504fb2d72729f2928345a notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```mysql

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;

```
