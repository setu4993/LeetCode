# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head and head.next and k > 0:
            k_list = [head]
            current = head.next
            prev = head
            n = 1
            while current:
                if len(k_list) == k:
                    prev = k_list.pop(0)
                k_list.append(current)
                current = current.next
                n += 1
            if k > n:
                k = k % n + n
            if n == k:
                pass
            elif len(k_list) == k:
                k_list[-1].next = head
                head = k_list[0]
                prev.next = None
            else:
                k_list[-1].next = head
                k_list[-k + n - 1].next = None
                head = k_list[- k + n]
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

l1 = CreateList([1, 2])

print(PrintList(Solution().rotateRight(l1, 3)))