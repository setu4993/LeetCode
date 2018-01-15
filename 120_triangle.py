class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        soln = [[0 for _ in range(0, len(triangle[i]))] for i in range(0, len(triangle))]
        soln[-1] = triangle[-1]
        for i in range(len(soln) - 2, -1, -1):
            for j in range(len(soln[i])):
                soln[i][j] = triangle[i][j] + min(soln[i + 1][j:j + 2])
        return soln[0][0]

print(Solution().minimumTotal([[-1],[3,2],[-3,1,-1]]))

print(Solution().minimumTotal([[-1],[-3,-4]]))