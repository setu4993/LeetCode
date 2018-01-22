class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) > 2:
            mid = int(n / 2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                return mid + self.findPeakElement(nums[mid:])
            else:
                return self.findPeakElement(nums[:mid + 1])
        elif n == 2:
            return 1 if nums[1] > nums[0] else 0
        else:
            return 0

print(Solution().findPeakElement([2, 1]))