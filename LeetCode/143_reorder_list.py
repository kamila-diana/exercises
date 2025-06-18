# LeetCode 143. Reorder List
from math import ceil
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    last_node = None
    node = head
    while node:
        next_node = node.next
        node.next = last_node
        last_node = node
        node = next_node
    return last_node


def mergeList(head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
    # assumption: len(head1) = len(head2) or len(head2) + 1
    node1 = head1
    node2 = head2
    while node1 and node2:
        next1 = node1.next
        next2 = node2.next
        node1.next = node2
        node2.next = next1
        node1 = next1
        node2 = next2


def reorderList(head: Optional[ListNode]) -> None:
    size = 0
    i = head
    while i:
        size += 1
        i = i.next
    i = head
    steps = ceil(size / 2) - 1
    for j in range(0, steps):
        i = i.next
    second_half = i.next
    i.next = None

    reversed_half = reverseList(second_half)
    mergeList(head, reversed_half)


if __name__ == "__main__":
    a = ListNode(4, None)
    b = ListNode(3, a)
    c = ListNode(2, b)
    reorderList(c)
    assert (c.val, c.next.val, c.next.next.val) == (2, 4, 3)