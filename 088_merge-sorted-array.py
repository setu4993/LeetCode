class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                i += 1

        while j < n:
            nums1.append(nums2[j])
            j += 1

        print(nums1)

Solution().merge([0, 2, 4], 3, [1, 3, 5, 6], 4)