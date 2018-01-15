# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def CreateList(self, num_list):
        head = n = ListNode(0)
        for l in num_list:
            n.next = ListNode(l)
            n = n.next
        return head.next


    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        seq = []
        dups = []
        if current:
            while current:
                if current.val not in dups:
                    if current.val in seq:
                        seq.remove(current.val)
                        dups.append(current.val)
                    else:
                        seq.append(current.val)
                current = current.next
            return self.CreateList(seq)
        return head


def PrintList(current):
    numbers = []
    while current:
        numbers.append(current.val)
        current = current.next
    return numbers

head = Solution().CreateList([1, 2, 3, 3, 4, 4, 5])
print(PrintList(Solution().deleteDuplicates(head)))