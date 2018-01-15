class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        sol = [1]
        if rowIndex >= 1:
            i = 1
            while i < rowIndex + 1:
                loc = []
                loc.append(sol[0])
                for j in range(1, i):
                    loc.append(sol[j - 1] + sol[j])
                loc.append(sol[i - 1])
                sol = loc
                i += 1
        return sol

print(Solution().getRow(1))