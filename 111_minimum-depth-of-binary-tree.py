class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_depth = 0
        if root:
            if root.left and root.right:
                min_depth = min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left:
                min_depth = self.minDepth(root.left)
            elif root.right:
                min_depth = self.minDepth(root.right)
            return 1 + min_depth
        else:
            return min_depth


p = TreeNode(1)
p.left = TreeNode(9)
p.right = n = TreeNode(20)
n.left = TreeNode(15)
n.right = TreeNode(7)

print(Solution().minDepth(p))