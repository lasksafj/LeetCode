# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = 0
        res = root
        def dfs(r, d):
            nonlocal cur,res
            if not r: return d
            a = dfs(r.left, d+1)
            b = dfs(r.right, d+1)
            if a == b:
                if a >= cur:
                    cur = a
                    res = r
            return max(a,b)
        dfs(root, 0)
        return res