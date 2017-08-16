class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring_list = []
        substring = []
        for char in s:
            if char not in substring:
                substring.append(char)
            else:
                substring_list.append("".join(substring))
                substring = substring[substring.index(char) + 1:len(substring)]
                substring.append(char)
        substring_list.append("".join(substring))
        return len(max(substring_list, key=len))

print(Solution().lengthOfLongestSubstring("bpfbhmipx"))