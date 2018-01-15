# import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** (1 / 2)) #python 3
        # return int(x ** (1 / 2.0)) #python 2

print(Solution().mySqrt(4))