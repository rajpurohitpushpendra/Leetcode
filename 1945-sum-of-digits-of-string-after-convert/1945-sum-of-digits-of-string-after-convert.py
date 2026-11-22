class Solution:
    def getLucky(self, s, k):
        num = ""

        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        result = int(num)

        for _ in range(k):
            result = sum(int(digit) for digit in str(result))

        return result