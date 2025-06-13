# LeetCode 206. Reverse Linked List

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


if __name__ == "__main__":
    a = ListNode(2, None)
    b = ListNode(1, a)
    c = ListNode(0, b)
    result = reverseList(c)
    print(result.val, result.next.val, result.next.next.val)


