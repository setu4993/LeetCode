# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root:
            val = root.val
            if val == sum and root.left == root.right == None:
                return [[val]]
            else:
                left = self.pathSum(root.left, sum - val)
                right = self.pathSum(root.right, sum - val)
                current = []
                for c in left + right:
                    c.insert(0, val)
                    current.append(c)
                return current
        return []

p = TreeNode(1)
p.left = TreeNode(9)
p.right = n = TreeNode(20)
n.left = TreeNode(15)
n.right = TreeNode(7)

print(Solution().pathSum(p, 36))