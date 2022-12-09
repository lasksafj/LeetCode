# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(r, mi, ma):
            if not r:
                return
            mi = min(mi, r.val)
            ma = max(ma, r.val)
            res[0] = max(res[0], ma-mi)
            dfs(r.left, mi, ma)
            dfs(r.right, mi, ma)
        dfs(root, inf, -inf)
        return res[0]
            
            