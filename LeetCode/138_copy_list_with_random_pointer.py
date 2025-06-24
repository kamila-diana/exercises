# LeetCode 138. Copy List with Random Pointer
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def print_node(self):
        print(self.val, self)


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    map_to_copy = {}
    node = head
    while node:
        new_node = Node(node.val, node.next, node.random)
        map_to_copy[node] = new_node
        node = node.next

    node = head
    while node:
        if node.next:
            map_to_copy[node].next = map_to_copy[node.next]
        if node.random:
            map_to_copy[node].random = map_to_copy[node.random]
        node = node.next

    if head:
        return map_to_copy[head]
    else:
        return None


if __name__ == "__main__":
    b = Node(2, None, None)
    a = Node(1, b, None)
    result = copyRandomList(a)
