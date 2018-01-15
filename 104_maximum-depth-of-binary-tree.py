class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0
        if root:
            if root.left and root.right:
                max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
            elif root.left:
                max_depth = self.maxDepth(root.left)
            elif root.right:
                max_depth = self.maxDepth(root.right)
            return 1 + max_depth
        else:
            return max_depth


p = TreeNode(1)
p.left = TreeNode(9)
p.right = n = TreeNode(20)
n.left = TreeNode(15)
n.right = TreeNode(7)

print(Solution().maxDepth(p))