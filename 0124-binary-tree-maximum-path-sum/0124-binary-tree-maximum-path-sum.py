# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-inf]
        def dfs(r):
            if not r:
                return -100000
            a = dfs(r.left)
            b = dfs(r.right)
            c = a + b + r.val
            d = a + r.val
            e = b + r.val
            res[0] = max(res[0], a, b, c, d, e, r.val)
            return max(r.val, d, e)
        dfs(root)
        return res[0]