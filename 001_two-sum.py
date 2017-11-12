class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        differences = {}
        for i, n in enumerate(nums):
            if n in differences:
                return differences[nums[i]], i
            else:
                differences[target - n] = i
        return -1, -1

print(Solution().twoSum([2, 7, 11, 15], 9))