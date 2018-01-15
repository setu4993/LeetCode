class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while 0 < m and 0 < n:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        while 0 < n:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


Solution().merge([1, 3, 5, 7], 4, [0, 2, 4, 6], 4)