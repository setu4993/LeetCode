class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        working = []
        parentheses_dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in parentheses_dict.values():
                working.append(char)
            elif char in parentheses_dict.keys() and working and (working[-1] == parentheses_dict[char]):
                working.pop()
            else:
                return False
        if not working:
            return True
        else:
            return False

print(Solution().isValid("{}()[]()()[{()}(]"))