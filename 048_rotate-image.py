class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for j in range(int(n/2)):
            for i in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp
        print(matrix)

Solution().rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])