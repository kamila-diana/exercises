# Leetcode 110. Balanced Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.balanced = None

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def rec(node: Optional[TreeNode]):
            if node:
                left = rec(node.left)
                right = rec(node.right)
                if abs(left - right) > 1:
                    self.balanced = False
                return max(left, right) + 1
            else:
                return 0

        rec(root)
        return self.balanced


if __name__ == "__main__":
    a = TreeNode(2, None, None)
    b = TreeNode(1, None, a)
    s = Solution()
    assert s.isBalanced(b)
