class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        converted = [''] * numRows
        row = 0
        i = 0
        down = True
        if numRows > 1:
            while i < len(s):
                converted[row] += s[i]
                if down and row != (numRows - 1):
                    row += 1
                elif down and row == (numRows - 1):
                    down = not down
                    row -= 1
                elif not down and row == 0:
                    down = not down
                    row += 1
                elif not down:
                    row -= 1
                i += 1
        else:
            return s
        '''
        col = 0
        while row < numRows:
            row_text = []
            while col < len(s):
                row_text.append(s[col])
                print(row, col, s[col])
                col += 2 * (numRows - 1)
            row += 1
            col = row
            converted = converted + ''.join(row_text)

        
        for i in range(len(s)):
            location = i % len(s)
            converted.append(s[i])
        return ''.join(converted)
        '''
        return ''.join(converted)


print(Solution().convert("PAYPALISHIRING", 4))