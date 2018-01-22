# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # iterative
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
        """
        # recursive
        def recurse(prev, head):
            if head:
                curr = head
                head = head.next
                curr.next = prev
                return recurse(curr, head)
            else:
                return prev

        return recurse(None, head)

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

l1 = CreateList([1, 2, 3])
print(PrintList(l1))
print(PrintList(Solution().reverseList(l1)))