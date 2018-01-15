# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            val = root.val
            if val == sum and root.left == root.right == None:
                return True
            else:
                return self.hasPathSum(root.left, sum - val) or self.hasPathSum(root.right, sum - val)
        return False

p = TreeNode(1)
p.left = TreeNode(9)
p.right = n = TreeNode(20)
n.left = TreeNode(15)
n.right = TreeNode(7)

print(Solution().hasPathSum(p, 36))