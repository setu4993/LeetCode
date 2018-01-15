class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        try:
            if nums.index(target) >= 0:

                return True
        except ValueError:
            return False

print(Solution().search([1], 1))