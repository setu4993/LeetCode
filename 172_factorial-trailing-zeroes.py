import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes = 0
        while n >= 5:
            zeroes += int(n / 5)
            n /= 5
        return zeroes

print(Solution().trailingZeroes(5))