# using a ring buffer
# beat 99.8% of submissions

from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not n or n == 1 and not head.next:
            return None
        node = head
        tail_nodes, total_count = find_tail_nodes(head, n)
        return unlink_first_node(tail_nodes, n, total_count) or head

def find_tail_nodes(node, n):
    counter = 0
    ring_buffer = deque(maxlen = n + 1)
    while node:
        ring_buffer.append(node)
        node = node.next
        counter += 1

    return ring_buffer, counter


def unlink_first_node(nodes, n, count):
    if len(nodes) < 2:
        return
    elif len(nodes) == 2:
        nodes[0].next = None
    else:
        nodes[0].next = nodes[2]

    if count < n:
        return nodes[0] if n & 1 else nodes[1]
    if count == n:
        return nodes[1]
