class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = int(len(nums) / 2)
        if nums and l == 0 and nums[l] == target:
            return [0, 0]
        elif l > 0:
            if nums[l] < target:
                j, k = Solution().searchRange(nums[l:], target)
                if j != -1:
                    j += l
                    k += l
            elif nums[l] > target:
                j, k = Solution().searchRange(nums[:l], target)
            else:
                j1, k1 = Solution().searchRange(nums[:l], target)
                j2, k2 = Solution().searchRange(nums[l:], target)
                if j1 != -1:
                    if j2 != -1:
                        j, k = j1, k2 + l
                    else:
                        j, k = j1, k1
                elif j2 != -1:
                    j, k = j2 + l, k2  + l
                else:
                    j, k = -1, -1
            return [j, k]
        else:
            return [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

print(Solution().searchRange([], 3))