# LeetCode 2. Add Two Numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listToNumber(l: Optional[ListNode]) -> int:
    result = ""
    node = l
    while node:
        result = str(node.val) + result
        node = node.next
    return int(result)


def numberToList(n: int) -> Optional[ListNode]:
    s = str(n)
    node = None
    while s:
        node = ListNode(val=int(s[0]), next=node)
        s = s[1:]
    return node


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    return numberToList(listToNumber(l1) + listToNumber(l2))


if __name__ == "__main__":
    assert addTwoNumbers(ListNode(1), ListNode(3)).val == 4
