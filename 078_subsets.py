class Solution:
    def combine(self, nums, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            soln = [[]]
        elif k == 1:
            soln = [[i] for i in nums]
        elif len(nums) - k == 0:
            soln = [nums]
        else:
            soln = self.combine(nums[:-1], k)
            below = self.combine(nums[:-1], k - 1)
            for b in below:
                if b:
                    b.append(nums[-1])
                    soln.append(b)
        return soln

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        soln = []
        for i in range(len(nums) + 1):
            soln += self.combine(nums, i)
        return soln

print(Solution().subsets([1, 2, 3]))