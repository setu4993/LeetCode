class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = nums[0]
        for n in nums[1:]:
            if n < f:
                return n

        return f

print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))