class Solution:
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        differences = {}
        for i, n in enumerate(numbers):
            if n in differences:
                return differences[numbers[i]], i + 1
            else:
                differences[target - n] = i + 1
        return 0, 0

print(Solution().twoSum([2, 7, 11, 15], 9))