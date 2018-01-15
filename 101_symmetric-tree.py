# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_tree(array):
    stack = []
    root = TreeNode(array[0])
    stack.append(root)
    for i in range(1, len(array)):
        node = TreeNode(array[i])
        stack.append(node)
        if i % 2 == 0:
            stack[int((i - 1) / 2)].left = node
        else:
            stack[int((i - 1) / 2)].right = node
    return root


def inorderTraversal(root):
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

class Solution:
    def mirror(self, left, right):
        if left == right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val == right.val:
            return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
        else:
            return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.mirror(root.left, root.right)



root = array_to_tree([1, 2, 2, 3, None, None, 1])
print(Solution().isSymmetric(root))