class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        mn, mx = min(nums), max(nums)

        if mn == mx:
            return 0

        n = len(nums)
        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count

        for num in nums:
            i = (num - mn) // bucket_size
            bucket_min[i] = min(bucket_min[i], num)
            bucket_max[i] = max(bucket_max[i], num)
            used[i] = True

        ans = 0
        prev = mn

        for i in range(bucket_count):
            if used[i]:
                ans = max(ans, bucket_min[i] - prev)
                prev = bucket_max[i]

        return ans