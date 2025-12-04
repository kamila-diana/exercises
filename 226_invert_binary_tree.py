# LeetCode 226. Invert Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        return TreeNode(root.val, invertTree(root.right), invertTree(root.left))
    else:
        return None


if __name__ == "__main__":
    a = TreeNode(2, None, None)
    b = TreeNode(1, None, a)
    result = invertTree(b)
