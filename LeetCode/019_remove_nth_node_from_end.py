# LeetCode 19. Remove Nth Node From End of List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_size(h: Optional[ListNode]) -> int:
    size = 0
    i = h
    while i:
        size += 1
        i = i.next
    return size


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    size = list_size(head)
    if size > 1:
        steps = size - n - 1
        if steps >= 0:
            i = head
            while steps > 0:
                i = i.next
                steps -= 1
            i.next = i.next.next
        else:
            head = head.next
    else:
        head = None
    return head


if __name__ == "__main__":
    a = ListNode(4, None)
    b = ListNode(3, a)
    c = ListNode(2, b)
    removeNthFromEnd(c, 2)
    assert (c.val, c.next.val, c.next.next) == (2, 4, None)
