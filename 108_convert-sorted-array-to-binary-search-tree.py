# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            if len(nums) > 2:
                node = TreeNode(nums[int(len(nums)/2)])
                node.left = self.sortedArrayToBST(nums[:int(len(nums)/2)])
                node.right = self.sortedArrayToBST(nums[int(len(nums)/2) + 1:])
            elif len(nums) == 2:
                node = TreeNode(nums[1])
                node.left = TreeNode(nums[0])
            else:
                node = TreeNode(nums[0])
            return node
        else:
            return None


print(Solution().sortedArrayToBST([1, 2, 3]))