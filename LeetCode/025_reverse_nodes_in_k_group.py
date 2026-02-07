# LeetCode 25. Reverse Nodes in k-Group
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        node = head
        while node:
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node
        return last_node

    def cut(self, head: ListNode, k: int) -> ListNode:
        i = 1
        node = head
        while i < k and node.next:
            node = node.next
            i += 1
        result = node.next
        node.next = None
        return result

    def size_linked_list(self, head: Optional[ListNode]) -> int:
        node = head
        i = 0
        while node:
            node = node.next
            i += 1
        return i

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = self.size_linked_list(head)
        number_of_groups = size // k
        if number_of_groups == 0:
            return head

        node = head
        next = self.cut(node, k)
        reversed_group = self.reverseList(node)
        result = reversed_group
        last_node = node
        node = next
        for i in range(1, number_of_groups):
            next = self.cut(node, k)
            reversed_group = self.reverseList(node)
            last_node.next = reversed_group
            last_node = node
            node = next
        last_node.next = node
        return result


if __name__ == "__main__":
    s = Solution()
    a = ListNode(2, None)
    b = ListNode(1, a)
    c = ListNode(0, b)
    test_1 = s.reverseKGroup(a, 1)
    assert test_1.val == 2
    test_2 = s.reverseKGroup(c, 2)
    assert (test_2.val, test_2.next.val, test_2.next.next.val) == (1, 0, 2)
