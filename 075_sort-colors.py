class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        for j in range(1, len(colors)):
            colors[j] += colors[j - 1]
        colors.insert(0, 0)
        for j, color in enumerate(colors):
            while color > colors[j - 1]:
                nums[color - 1] = j - 1
                color -= 1
        print(nums)


Solution().sortColors([1, 2, 2, 1, 2, 2, 0, 0, 0])