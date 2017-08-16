class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = []
        if strs:
            shortest = min(strs, key=len)
            for i in range(len(shortest)):
                for s in strs:
                    if s[i] == strs[0][i]:
                        pass
                    else:
                        return "".join(common)
                common.append(strs[0][i])
        return "".join(common)

print(Solution().longestCommonPrefix(["aaa", "aaaaa", "aaaaaaa"]))