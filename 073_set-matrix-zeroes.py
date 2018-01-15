class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            rows = []
            cols = []
            for i, row in enumerate(matrix):
                for j, cel in enumerate(row):
                    if cel == 0:
                        rows.append(i)
                        cols.append(j)

            for r in rows:
                matrix[r] = [0 for _ in range(n)]
            for c in cols:
                for i in range(m):
                    matrix[i][c] = 0
            print(matrix)

Solution().setZeroes([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
