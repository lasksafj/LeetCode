# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def sol(cur, a):
            if not cur:
                return 0
            res = cur.val * a
            for ne in [cur.left, cur.right]:
                if a:
                    res += sol(ne, 0)
                else:
                    res += max(sol(ne, 0), sol(ne, 1))
            return res
        return max(sol(root, 0), sol(root, 1))