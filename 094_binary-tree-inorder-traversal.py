# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = []
        nodes = []
        current = root
        while current:
            if current.left:
                nodes.append(current)
                tmp = current
                current = current.left
                tmp.left = None
            elif current.right:
                temp.append(current.val)
                tmp = current
                current = current.right
                tmp.right = None
            else:
                temp.append(current.val)
                if nodes:
                    current = nodes.pop()
                else:
                    current = None
        return temp

tree_a = TreeNode(1)
tree_a_b = tree_a.right = TreeNode(2)
tree_a_b.left = TreeNode(3)

print(Solution().inorderTraversal(tree_a))