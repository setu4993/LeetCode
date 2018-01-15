class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = 0
        for i, num in enumerate(nums):
            if i > jump:
                return False
            jump = max(jump, i + num)
        return True


print(Solution().canJump([3, 2, 0, 0, 4]))