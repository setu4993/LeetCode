import re, math

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+', '', s).lower()
        if s[:int(len(s)/2)] == s[int((len(s) + 1)/2):][::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome("aaab"))