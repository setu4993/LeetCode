# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def PrintList(current):
    numbers = []
    while current:
        numbers.append(current.val)
        current = current.next
    return numbers


class Solution(object):
    def CreateList(self, num_list):
        head = n = ListNode(0)
        for l in num_list:
            n.next = ListNode(l)
            n = n.next
        return head.next

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lesser = []
        greater = []
        while head:
            if head.val < x:
                lesser.append(head.val)
            else:
                greater.append(head.val)
            head = head.next
        if lesser or greater:
            lower = self.CreateList(lesser)
            if lower:
                current = lower
                while current.next:
                    current = current.next
                current.next = self.CreateList(greater)
                return lower
            else:
                return self.CreateList(greater)
        else:
            return head

print(PrintList(Solution().partition(Solution().CreateList([1]), 0)))