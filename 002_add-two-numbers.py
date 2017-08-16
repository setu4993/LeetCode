# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = current = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            carry, step_val = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(step_val)
            current = current.next

        return head.next


def CreateList(num_list):
    head = n = ListNode(0)
    for l in num_list:
        n.next = ListNode(l)
        n = n.next
    return head.next

l1 = CreateList([2, 4, 3])

l2 = CreateList([5, 6, 4])

Solution().addTwoNumbers(l1, l2)