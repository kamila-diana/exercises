# LeetCode 543. Diameter of Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def rec(r: Optional[TreeNode]) -> int:
            if r:
                left = rec(r.left)
                right = rec(r.right)
                self.diameter = max(self.diameter, left + right)
                return max(left, right) + 1
            else:
                return 0

        rec(root)
        return self.diameter


if __name__ == "__main__":
    a = TreeNode(2, None, None)
    b = TreeNode(1, None, a)
    s = Solution()
    assert s.diameterOfBinaryTree(b) == 1
