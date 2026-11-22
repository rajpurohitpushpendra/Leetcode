class Solution:
    def divide(self, dividend, divisor):
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            quotient = quotient + multiple

        if sign == -1:
            quotient = 0 - quotient

        if quotient > 2**31 - 1:
            return 2**31 - 1

        if quotient < -2**31:
            return -2**31

        return quotient