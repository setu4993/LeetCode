class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def recurse(s, k, curr):
            if s:
                for i in range(1, min(4, len(s) + 1)):
                    if i == 3 and int(s[:i]) > 255:
                        continue
                    elif i > 1 and s[0] == '0':
                        continue
                    else:
                        recurse(s[i:], k + 1, curr + [s[:i]])
            elif k == 4:
                soln.append(".".join(curr))
        soln = []
        if len(s) <= 12:
            recurse(s, 0, [])
        return soln

print(Solution().restoreIpAddresses("25525511135"))