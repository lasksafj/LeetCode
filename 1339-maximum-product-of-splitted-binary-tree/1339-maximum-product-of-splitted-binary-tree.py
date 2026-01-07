# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def ssum(r):
            if not r: return 0
            return r.val + ssum(r.left) + ssum(r.right)
        s = ssum(root)
        res = 0
        def dfs(r):
            nonlocal res
            if not r: return 0
            ne_s = 0
            for ne in [r.left, r.right]:
                b = dfs(ne)
                ne_s += b
                res = max(res, b * (s - b))
            return r.val + ne_s
        dfs(root)
        return res % (10**9+7)