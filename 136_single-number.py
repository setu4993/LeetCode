class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            nums.sort()
            i = 1
            while i < len(nums):
                if nums[i - 1] != nums[i]:
                    return nums[i - 1]
                else:
                    i += 2
            return nums[-1]
        else:
            return 0

print(Solution().singleNumber([2, 3, 4, 5, 0, 0, 1, 1, 2, 3, 4, 5, 6]))