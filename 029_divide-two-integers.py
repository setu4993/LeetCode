class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) is not (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        if divisor == 0:
            return 2147483647
        while dividend >= divisor:
            remainder = divisor
            current = 1
            while dividend >= remainder:
                dividend -= remainder
                quotient += current
                current <<= 1
                remainder <<= 1
        if negative:
            quotient = -quotient

        return min(quotient, 2147483647)

print(Solution().divide(-32, -2))
print(Solution().divide(-2147483648, -1))