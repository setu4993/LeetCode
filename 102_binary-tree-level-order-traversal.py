class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        soln = []
        if root:
            current_level = [root]
            while current_level:
                next_level = []
                soln.append([])
                for c in current_level:
                    soln[-1].append(c.val)
                    if c.left:
                        next_level.append(c.left)
                    if c.right:
                        next_level.append(c.right)
                current_level = next_level
        return soln

p = TreeNode(3)
p.left = TreeNode(9)
p.right = n = TreeNode(20)
n.left = TreeNode(15)
n.right = TreeNode(7)


print(Solution().levelOrder(p))