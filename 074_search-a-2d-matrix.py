class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = 0
        if matrix and matrix[j]:
            for i in matrix:
                if i[0] <= target:
                    j += 1
                else:
                    break
            try:
                print(matrix[j - 1])
                for m in matrix[j - 1]:
                    if m == target:
                        return True
            except IndexError:
                pass
        return False

print(Solution().searchMatrix([[1],[3]], 1))