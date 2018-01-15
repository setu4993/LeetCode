from math import factorial
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))

print(Solution().numTrees(3))