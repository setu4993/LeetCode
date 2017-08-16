# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            l3 = current = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = ListNode(l1.val)
                    current = current.next
                    l1 = l1.next
                else:
                    current.next = ListNode(l2.val)
                    current = current.next
                    l2 = l2.next
            if l1:
                current.next = l1
            elif l2:
                current.next = l2

            return l3.next

        if len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return lists
        else:
            middle = int(len(lists) / 2)
            left = Solution().mergeKLists(lists[:middle])
            right = Solution().mergeKLists(lists[middle:])
            return mergeTwoLists(left, right)


        # O (n log k) - divide and conquer


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

l1 = CreateList([2, 3, 4])
l2 = CreateList([1, 5, 6])
l3 = CreateList([0, 8, 9])
l4 = CreateList([7, 11])
l5 = CreateList([7, 10, 12])
l = Solution().mergeKLists([l1, l2, l3, l4, l5])
print(PrintList(l))