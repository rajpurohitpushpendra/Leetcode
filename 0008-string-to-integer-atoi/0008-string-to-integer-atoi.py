class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        # 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits
        result = 0

        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit

            i += 1

        # Step 4: Apply sign
        result = result * sign

        # Step 5: Handle overflow
        if result > INT_MAX:
            return INT_MAX

        if result < INT_MIN:
            return INT_MIN

        return result