# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if current:
            while current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current = current.next
                    continue
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

head = CreateList([1, 1, 2, 3, 3])
print(PrintList(Solution().deleteDuplicates(head)))