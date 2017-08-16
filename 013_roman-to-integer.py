class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        i = 0
        while i < len(s):

            try:
                val_i = roman_dict[s[i]]
            except IndexError:
                val_i = 0
            except KeyError:
                val_i = 0

            try:
                val_plus = roman_dict[s[i + 1]]
            except IndexError:
                val_plus = 0
            except KeyError:
                val_plus = 0

            if val_i >= val_plus:
                value = value + val_i
                i += 1
            else:
                value = value + val_plus - val_i
                i += 2
        return value


print(Solution().romanToInt("CVI"))