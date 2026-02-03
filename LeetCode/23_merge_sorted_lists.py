# LeetCode 23. Merge k Sorted Lists

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

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        non_empty_lists = [x for x in lists if x is not None]
        while non_empty_lists:
            vals = [x.val for x in non_empty_lists]
            min_val = min(vals)
            i = vals.index(min_val)
            if non_empty_lists[i].next:
                non_empty_lists[i] = non_empty_lists[i].next
            else:
                del non_empty_lists[i]
            new_result = ListNode(val=min_val, next=result)
            result = new_result
        return self.reverseList(result)


if __name__ == "__main__":
    s = Solution()
    a = ListNode(2, None)
    b = ListNode(1, a)
    c = ListNode(1, None)
    x = s.mergeKLists([c, b])
    assert [x.val, x.next.val, x.next.next.val] == [1, 1, 2]



