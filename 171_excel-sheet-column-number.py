class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        while s:
            num += (ord(s[-1]) - 64) * (26 ** i)
            s = s[:-1]
            i += 1
        return num

print(Solution().titleToNumber("BA"))