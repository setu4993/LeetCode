# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def get_next_node(node, n):
            if node:
                next_node, val = get_next_node(node.next, n)
                if val != n:
                    new_node = ListNode(node.val)
                    new_node.next = next_node
                else:
                    new_node = node.next
            else:
                return None, 1
            return new_node, val + 1

        head, node_count = get_next_node(head, n)
        return head


def CreateList(num_list):
    head = n = ListNode(0)
    for l in num_list:
        n.next = ListNode(l)
        n = n.next
    return head.next

def PrintList(current):
    numbers = []
    while current:
        numbers.append(current.val)
        current = current.next
    return numbers

l1 = CreateList([2, 4, 3, 5, 12, 13, 6, 23, 32, 1, 2])
print(PrintList(l1))

l2 = Solution().removeNthFromEnd(l1, 3)
print(PrintList(l2))