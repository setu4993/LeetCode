# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder:
            root = TreeNode(postorder.pop())
            ind = inorder.index(root.val)
            root.left = self.buildTree(inorder[:ind], postorder[:ind])
            root.right = self.buildTree(inorder[ind + 1:], postorder[ind:])
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

print(Solution().inorderTraversal(Solution().buildTree([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 5, 7, 6, 4])))