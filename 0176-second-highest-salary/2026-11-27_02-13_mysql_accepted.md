# 176. Second Highest Salary
  
<br>**Problem:** https://leetcode.com/problems/second-highest-salary/<br>

**Difficulty:** Medium<br>
**Topics:** Database<br>
**Language:** mysql<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-27 02:13 local time

**Runtime:** 257 ms (beats 87.63410000000003%)
**Memory:** 0 MB (beats 100%)


<!-- leetgit:submissionId=2204178924 codeHash=89040eae2c628d337b3438cd9f55b65ed8c3fb5a6c6e2ede43c0a3e64b010152 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```mysql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```
