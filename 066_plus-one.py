class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        return list(map(int, str(num)))


print(Solution().plusOne([123]))