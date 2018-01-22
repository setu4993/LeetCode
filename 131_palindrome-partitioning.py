class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        soln = []

        def recurse(s, curr):
            if s:
                for i in range(1, len(s) + 1):
                    if s[:i] == s[:i][::-1]:
                        recurse(s[i:], curr + [s[:i]])
            else:
                soln.append(curr)
        recurse(s, [])
        return soln

print(Solution().partition("aab"))