# 190. Reverse Bits
  
<br>**Problem:** https://leetcode.com/problems/reverse-bits/<br>

**Difficulty:** Easy<br>
**Topics:** Divide and Conquer, Bit Manipulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-22 22:47 local time

**Runtime:** 1 ms (beats 55.7586%)
**Memory:** 19.2 MB (beats 70.0354%)


<!-- leetgit:submissionId=2201419033 codeHash=cb976d1f96477e5cbed2716d2774b16dc61286f7df317451279fb2764d0d0cc4 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
```
