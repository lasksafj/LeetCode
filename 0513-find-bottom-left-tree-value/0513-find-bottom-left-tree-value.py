# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = 0
        dep = -1
        def dfs(r,d):
            nonlocal res,dep
            if not r:
                return
            if d > dep:
                res = r.val
                dep = d
            dfs(r.left, d+1)
            dfs(r.right, d+1)
        dfs(root,0)
        return res