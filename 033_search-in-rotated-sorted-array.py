class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 8))