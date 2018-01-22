# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListN
        """
        curr = head
        extra = ListNode(0)
        extra.next = curr
        if n > m:
            prev = extra
            for _ in range(m - 1):
                prev = curr
                curr = curr.next
            begin = prev
            end = curr
            temp = curr
            for _ in range(n - m + 1):
                curr = temp
                temp = temp.next
                curr.next = prev
                prev = curr
            begin.next = curr
            end.next = temp
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

l1 = CreateList([1, 2, 3, 4, 5, 6])
print(PrintList(l1))
print(PrintList(Solution().reverseBetween(l1, 1, 4)))