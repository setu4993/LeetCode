class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            for i in range(len(nums) - 1, 0, -1):
                if nums[i - 1] < nums[i]:
                    for j in reversed(range(i, len(nums))):
                        if nums[i - 1] < nums[j]:
                            nums[i - 1], nums[j] = nums[j], nums[i - 1]
                            break
                    nums[i:] = nums[i:][::-1]
                    return
            nums.reverse()

Solution().nextPermutation([4, 3, 1])