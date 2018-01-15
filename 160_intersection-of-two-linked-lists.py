# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            curA, curB = headA, headB
            len_A, len_B = 0, 0
            while curA:
                len_A += 1
                curA = curA.next
            while curB:
                len_B += 1
                curB = curB.next
            curA, curB = headA, headB
            diff = len_A - len_B
            if diff > 0:
                for _ in range(diff):
                    curA = curA.next
            elif diff < 0:
                for _ in range(- diff):
                    curB = curB.next
            while curA != curB:
                curA = curA.next
                curB = curB.next
            return curA
        return None


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

h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h1.next = h4
h4.next = h3
h2.next = h3

print(PrintList(Solution().getIntersectionNode(h1, h2)))