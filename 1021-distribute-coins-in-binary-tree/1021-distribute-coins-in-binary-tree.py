# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            l = dfs(cur.left)
            r = dfs(cur.right)
            res += abs(l) + abs(r)
            return l+r+cur.val-1
        dfs(root)
        return res