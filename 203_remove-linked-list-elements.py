# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        extra = ListNode(0)
        extra.next = head
        curr = head
        prev = extra
        while curr:
            if curr.val != val:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        return extra.next


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

l1 = CreateList([1, 2, 3, 1])
print(PrintList(l1))
print(PrintList(Solution().removeElements(l1, 1)))