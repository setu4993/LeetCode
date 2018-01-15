# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
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
            if temp == sorted(temp) and len(set(temp)) == len(temp):
                return True
            else:
                return False
        else:
            return True


tree_a = TreeNode(2)
tree_a.right = TreeNode(3)
tree_a.left = TreeNode(1)

print(Solution().isValidBST(tree_a))