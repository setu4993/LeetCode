class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        soln = []
        if matrix and matrix[0]:
            soln += matrix[0]
            del matrix[0]
        if matrix:
            for m in matrix:
                if m:
                    soln.append(m.pop())
        if matrix:
            soln += reversed(matrix[-1])
            del matrix[-1]
        if matrix:
            for m in reversed(matrix):
                if m:
                    soln.append(m.pop(0))
        if matrix:
            soln += self.spiralOrder(matrix)
        return soln


print(Solution().spiralOrder([[7], [9], [6]]))