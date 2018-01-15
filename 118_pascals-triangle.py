class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows >= 1:
            i = 1
            sol = [[1]]
            while i < numRows:
                loc = []
                loc.append(sol[i - 1][0])
                for j in range(1, i):
                    loc.append(sol[i - 1][j - 1] + sol[i - 1][j])
                loc.append(sol[i - 1][i - 1])
                sol.append(loc)
                i += 1
        else:
            sol = []
        return sol


print(Solution().generate(0))