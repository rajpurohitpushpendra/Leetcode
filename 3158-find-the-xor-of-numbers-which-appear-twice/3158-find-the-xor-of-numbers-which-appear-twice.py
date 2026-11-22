class Solution:
    def duplicateNumbersXOR(self, nums):
        ans = 0

        for num in set(nums):
            if nums.count(num) == 2:
                ans ^= num

        return ans