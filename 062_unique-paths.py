from math import factorial
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > 0 and n > 0:
            return int((factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1))))
        else:
            return 0