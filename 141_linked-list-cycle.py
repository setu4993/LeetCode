# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tort = head
        if head and head.next:
            hare = head.next
            while tort != hare:
                if tort:
                    tort = tort.next
                else:
                    return False
                if hare and hare.next:
                    hare = hare.next.next
                else:
                    return False
            return True
        return False

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

h1 = ListNode(3)
h2 = h1.next = ListNode(2)
h3 = h2.next = ListNode(0)
h4 = h3.next = ListNode(-4)
h4.next = h2
# h4.next = h4

print(Solution().hasCycle(h1))