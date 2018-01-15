class Solution(object):
    def climbStairs(self, n, hist = {}):
        """
        :type n: int
        :rtype: int
        """
        l_sum = 0
        if n - 1 > 0:
            if n - 1 not in hist:
                more1 = Solution().climbStairs(n - 1, hist)
                l_sum += more1
                hist[n - 1] = more1
            else:
                l_sum += hist[n - 1]
        elif n - 1 == 0:
            l_sum += 1
        if n - 2 > 0:
            if n - 2 not in hist:
                more2 = Solution().climbStairs(n - 2)
                l_sum += more2
                hist[n - 2] = more2
            else:
                l_sum += hist[n - 2]
        elif n - 2 == 0:
            l_sum += 1
        return l_sum

print(Solution().climbStairs(3))