# LeetCode 21. Merge Two Sorted Linked Lists
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # to assume list1.val < list2:
    if list1 and list2:
        if list2.val < list1.val:
            head = list2
            current = list2
            list2 = list2.next
        else:
            head = list1
            current = list1
            list1 = list1.next
    elif list1:
        return list1
    elif list2:
        return list2
    else:
        return None

    while list1 and list2:
        if list2.val < list1.val:
            current.next = list2
            current = list2
            list2 = list2.next
        else:
            current.next = list1
            current = list1
            list1 = list1.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return head


if __name__ == "__main__":
    a = ListNode(2, None)
    b = ListNode(1, a)
    c = ListNode(3, None)
    d = ListNode(0, c)
    result = mergeTwoLists(b, d)
    assert (result.val, result.next.val, result.next.next.val, result.next.next.next.val) == (0, 1, 2, 3)
