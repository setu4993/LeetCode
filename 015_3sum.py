class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
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

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

print(Solution().threeSum([0, 0, 0]))

print(Solution().threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]))

print(Solution().threeSum([-2, 0, 0, 2, 2]))