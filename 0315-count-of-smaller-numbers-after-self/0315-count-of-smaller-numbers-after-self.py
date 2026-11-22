
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        arr = list(enumerate(nums))

        def merge_sort(left, right):
            if right - left <= 1:
                return arr[left:right]

            mid = (left + right) // 2

            a = merge_sort(left, mid)
            b = merge_sort(mid, right)

            merged = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i][1] <= b[j][1]:
                    counts[a[i][0]] += j
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1

            while i < len(a):
                counts[a[i][0]] += j
                merged.append(a[i])
                i += 1

            while j < len(b):
                merged.append(b[j])
                j += 1

            return merged

        merge_sort(0, n)
        return counts
