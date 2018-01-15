class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 0:
            nums = [i for i in range(1, (n ** 2) + 1)]
            soln = [[0 for _ in range(n)] for _ in range(n)]
            loop = 0
            while nums:
                try:
                    for i in range(loop, n - loop):
                        soln[loop][i] = nums.pop(0)
                    for j in range(loop + 1, n - loop):
                        soln[j][n - 1 - loop] = nums.pop(0)
                    for i in range(n - 2 - loop, loop - 1, -1):
                        soln[n - loop - 1][i] = nums.pop(0)
                    for j in range(n - 2 - loop, loop, -1):
                        soln[j][loop] = nums.pop(0)
                except IndexError:
                    break
                loop += 1
            return soln
        else:
            return []



print(Solution().generateMatrix(5))