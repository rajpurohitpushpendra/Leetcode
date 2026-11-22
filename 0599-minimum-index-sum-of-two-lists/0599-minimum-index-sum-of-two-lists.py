class Solution:
    def findRestaurant(self, list1, list2):
        index = {s: i for i, s in enumerate(list1)}
        result = []
        min_sum = float('inf')

        for j, s in enumerate(list2):
            if s in index:
                total = index[s] + j

                if total < min_sum:
                    min_sum = total
                    result = [s]
                elif total == min_sum:
                    result.append(s)

        return result