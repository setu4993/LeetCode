class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[j - 1] and j > i + 1:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        # if [nums[i], nums[left], nums[right]] not in results:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        try:
                            while nums[left] == nums[left - 1]:
                                left += 1
                        except IndexError:
                            pass
                        try:
                            if nums[right] == nums[right + 1]:
                                right -= 1
                        except IndexError:
                            pass
        return results

# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

print(Solution().fourSum([0, 0, 0, 0], 0))

print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))