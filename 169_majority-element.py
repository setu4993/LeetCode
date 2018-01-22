class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            try:
                count[n] += 1
            except KeyError:
                count[n] = 1

        return max(count, key=count.get)

print(Solution().majorityElement([0,0,0,1,1]))