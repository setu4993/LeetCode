class Solution(object):
    def convert_int(self, num_string):
        num = 0
        for n in num_string:
            num = num * 10 + int(n)
        return num

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = self.convert_int(num1)
        n2 = self.convert_int(num2)

        return str(n1 * n2)


print(Solution().multiply("12", "12"))