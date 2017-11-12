class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        used = []
        if len(nums) > 1:
            for n, num in enumerate(nums):
                if num in used:
                    pass
                else:
                    used.append(num)
                    below = Solution().permuteUnique(nums[:n] + nums[n + 1:])
                    if below:
                        for bel in below:
                            bel.insert(0, num)
                            perms.append(bel)
        else:
            perms.append(nums)
        return perms

print(Solution().permuteUnique([1,1,2]))