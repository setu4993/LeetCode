class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = []
        cols = []
        sqrs = []
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != ".":
                    rows.append((i, char))
                    cols.append((j, char))
                    sqrs.append((int(i / 3), int(j / 3), char))
        if len(rows) == len(set(rows)) and len(cols) == len(set(cols)) and len(sqrs) == len(set(sqrs)):
            return True
        else:
            return False


print(Solution().isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))