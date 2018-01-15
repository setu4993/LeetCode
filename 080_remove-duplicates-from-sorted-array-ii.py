class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 2
        i = 0
        n = len(nums)
        if n >= 2:
            while j < n - i:
                if nums[j] == nums[j - 1] == nums[j - 2]:
                    a = nums.pop(j)
                    nums.insert(len(nums), a)
                    i += 1
                else:
                    j += 1
            return j
        else:
            return len(nums)


print(Solution().removeDuplicates([1, 1, 1, 1, 3, 3]))