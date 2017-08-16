class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = 0
        for n in nums:
            if n < target:
                pos += 1
            else:
                break
        return pos


print(Solution().insertPosition([1, 2, 3, 4, 5, 6], 5))