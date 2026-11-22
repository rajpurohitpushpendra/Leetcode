import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        best_start = heap[0][0]
        best_end = max_val

        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)

            if max_val - min_val < best_end - best_start:
                best_start, best_end = min_val, max_val

            if elem_idx + 1 == len(nums[list_idx]):
                break

            next_val = nums[list_idx][elem_idx + 1]
            max_val = max(max_val, next_val)
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

        return [best_start, best_end]