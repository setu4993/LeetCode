class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and Solution().isSameTree(p.left, q.left) and Solution().isSameTree(p.right, q.right)
        else:
            return p is q

tree_a = TreeNode(1)
tree_a.left = TreeNode(2)
tree_a.right = TreeNode(2)

tree_b = TreeNode(1)
tree_b.left = TreeNode(2)
tree_b.right = TreeNode(2)

print(Solution().isSameTree(tree_a, tree_b))