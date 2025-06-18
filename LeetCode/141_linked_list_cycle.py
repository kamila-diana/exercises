# LeetCode 141. Linked List Cycle
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next
    increase_slow = False
    while fast:
        if fast == slow:
            return True
        else:
            fast = fast.next
            if increase_slow:
                slow = slow.next
                increase_slow = False
            else:
                increase_slow = True
    return False


if __name__ == "__main__":
    a = ListNode(2, None)
    b = ListNode(1, a)
    print(hasCycle(b))
