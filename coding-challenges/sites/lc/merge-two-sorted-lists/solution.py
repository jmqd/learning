class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []
        elif not l1:
            return l2
        elif not l2:
            return l1

        root, head, tail = (l1, l1, l2) if l1.val <= l2.val else (l2, l2, l1)

        while tail:
            if head.next is None:
                head.next = tail
                break
            elif tail.val < head.next.val:
                head.next, tail = tail, head.next
                head = head.next
            else:
                head = head.next

        return root
