class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        area = 0
        while i < j:
            area = max(area, (min(height[i], height[j]) * (j - i)))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area

print(Solution().maxArea([2, 3, 5, 12, 4, 2, 4, 1]))