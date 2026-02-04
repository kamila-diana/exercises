# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == "__main__":
    a = TreeNode(2)
    b = TreeNode(1)
    b.right = a
    s = Solution()
    assert s.lowestCommonAncestor(b, a, b).val == 1
