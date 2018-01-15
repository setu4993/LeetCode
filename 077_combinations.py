class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            soln = [[]]
        elif k == 1:
            soln = [[i] for i in range(1, n + 1)]
        elif n - k == 0:
            soln = [[i for i in range(1, n + 1)]]
        else:
            soln = self.combine(n - 1, k)
            below = self.combine(n - 1, k - 1)
            for b in below:
                if b:
                    b.append(n)
                    soln.append(b)
        return soln


print(Solution().combine(4, 3))