# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            root = TreeNode(preorder.pop(0))
            ind = inorder.index(root.val)
            root.left = self.buildTree(preorder[:ind], inorder[:ind])
            root.right = self.buildTree(preorder[ind:], inorder[ind + 1:])
            return root
        return None


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

print(Solution().inorderTraversal(Solution().buildTree([4, 2, 1, 3, 5], [1, 2, 3, 4, 5])))