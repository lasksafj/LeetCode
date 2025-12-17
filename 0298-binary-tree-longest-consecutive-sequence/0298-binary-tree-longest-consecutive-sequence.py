# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r, l, p):
            nonlocal res
            if not r:
                return
            if r.val == p+1:
                l += 1
            else:
                l = 1
            res = max(res, l)
            p = r.val
            dfs(r.left, l, p)
            dfs(r.right, l, p)
        dfs(root, 1, -inf)
        return res