# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = current = ListNode(0)
        current.next = head
        prev_node = current
        current = current.next
        while current:
            temp = current.next
            if temp:
                current.next = temp.next
                temp.next = current
                current = current.next
                prev_node.next = temp
                prev_node = temp.next
            else:
                break

        return new_head.next
        # a -> b -> c -> d
        # b -> a -> d -> c


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

l1 = CreateList([2, 3, 4, 5, 6, 7])
l = Solution().swapNodes(l1)
print(PrintList(l))