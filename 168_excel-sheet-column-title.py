class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        soln = ""
        while n > 0:
            soln = chr(65 + ((n - 1) % 26)) + soln
            n = (n - 1) // 26
        return soln

print(Solution().convertToTitle(52))