class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        if len(nums) > 1:
            for n in range(len(nums)):
                below = Solution().permute(nums[:n] + nums[n+1:])
                if below:
                    for bel in below:
                        bel.insert(0, nums[n])
                        perms.append(bel)
        else:
            perms.append(nums)
        return perms

print(Solution().permute([1, 1, 2]))