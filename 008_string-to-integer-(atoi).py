class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        value = 0
        try:
            if str[0] == '-':
                neg = True
                str = str[1:]
            elif str[0] == '+':
                neg = False
                str = str[1:]
            else:
                neg = False
        except IndexError:
            return value
        for s in str:
            if s in num_dict:
                value = value * 10 + num_dict[s]
            else:
                break

        if neg:
            value = 0 - value

        if value > 2147483647:
            return 2147483647

        if value < -2147483648:
            return -2147483648

        return value

v = Solution().myAtoi('   -124a2324')
print(v, type(v))