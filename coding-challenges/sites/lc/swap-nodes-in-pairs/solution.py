'''
Leetcode 24 submission
Your runtime beats 90.27 % of python3 submissions.
'''
from collections import deque as _deque

class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

def solve(head):
    # simple return cases
    if head and head.next:
        deque = _deque()
        deque.append(head)
        deque.append(head.next)
        head = head.next
    else:
        return head

    while len(deque) >= 2:
        # swap the latest pair's pointer
        deque[-2].next, deque[-1].next = deque[-1].next, deque[-2]

        # swap them in the deque so they make sequential sense
        deque[-1], deque[-2] = deque[-2], deque[-1]

        # update the rightmost of the previous pair as it's neighbor changed
        if len(deque) > 2:
            deque[-3].next = deque[-2]

        # the leftmost element is now totally complete, so we pop it
        deque.popleft()

        # enqueue iff another non-null pair to swap is possible
        if deque[-1].next and deque[-1].next.next:
            deque.append(deque[-1].next)
            deque.append(deque[-1].next)
        else:
            break

    return head

def execute_tests():
    simple = ListNode(1)
    simple.next = ListNode(2)
    simple.next.next = ListNode(3)
    simple.next.next.next = ListNode(4)

    ans = "2143"

    for test_case in [(simple, ans)]:
        test(*test_case)

def test(head, expected):
    answer = solve(head)
    print(as_string((answer)))
    assert as_string(answer) == expected

def as_string(head):
    s = ''
    while head:
        s += str(head.x)
        head = head.next
    return s

def main():
    return execute_tests()

if __name__ == '__main__':
    main()
