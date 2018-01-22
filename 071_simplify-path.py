class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        soln = []
        for s in path.split("/"):
            if s == '..':
                if soln:
                    soln.pop()
            elif s and s != '.':
                soln.append(s)
        return "/" + "/".join(soln)


print(Solution().simplifyPath("/../"))