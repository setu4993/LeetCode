class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        current_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            # if nums[i] == nums[i - 1] and i > 0:
            #     continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum >= target:
                    right -= 1
                elif sum < target:
                    left += 1
                if abs(current_sum - target) > abs(sum - target):
                    current_sum = sum
                    print(current_sum)
        return current_sum

# print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

print(Solution().threeSumClosest([0, 1, 2], 3))
