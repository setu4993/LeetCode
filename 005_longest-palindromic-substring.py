class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(len(s) - 1, 0, -1):
            for j in range(0, len(s) - i):
                substring = s[j:j + i + 1]
                if substring == substring[::-1]:
                    return substring

print(Solution().longestPalindrome("ababad"))