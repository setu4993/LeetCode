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

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        soln = []
        for i in range(len(nums) + 1):
            out += self.combine(nums, i)
        for o in out:
            if o not in soln:
                soln.append(o)
        return soln

print(Solution().subsetsWithDup([1, 2, 2]))