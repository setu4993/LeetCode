# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = []
        nodes = []
        current = root
        while current:
            temp.append(current.val)
            if current.left and current.right:
                nodes.append(current.right)
                current = current.left
            elif current.left:
                current = current.left
            elif current.right:
                current = current.right
            elif nodes:
                current = nodes.pop()
            else:
                current = None
        return temp


tree_a = TreeNode(1)
tree_a_b = tree_a.right = TreeNode(2)
tree_a.left = TreeNode(0)
tree_a_b.right = TreeNode(4)
tree_a_b.left = TreeNode(3)

print(Solution().preorderTraversal(tree_a))