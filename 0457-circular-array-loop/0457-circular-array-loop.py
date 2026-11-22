class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        for i in range(n):
            slow = fast = i
            direction = nums[i] > 0

            while True:
                if (nums[slow] > 0) != direction:
                    break

                next_slow = (slow + nums[slow]) % n

                if (nums[fast] > 0) != direction:
                    break
                next_fast = (fast + nums[fast]) % n

                if (nums[next_fast] > 0) != direction:
                    break
                next_fast = (next_fast + nums[next_fast]) % n

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False