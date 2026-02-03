# LeetCode 100. Same Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.same = None

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def rec(t_1: Optional[TreeNode], t_2: Optional[TreeNode]):
            if t_1 and t_2:
                if t_1.val == t_2.val:
                    rec(t_1.left, t_2.left)
                    rec(t_1.right, t_2.right)
                else:
                    self.same = False
            elif t_1 or t_2:
                self.same = False
            else:
                pass

        rec(p, q)
        return self.same


if __name__ == "__main__":
    a = TreeNode(2, None, None)
    b = TreeNode(1, None, a)
    s = Solution()
    assert not s.isSameTree(a, b)
    assert s.isSameTree(b, b)
