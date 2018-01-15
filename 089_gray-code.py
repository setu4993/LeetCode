class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray = []
        for i in range(0, 1 << n):
            gray.append(i ^ (i >> 1))
        return gray

print(Solution().grayCode(4))