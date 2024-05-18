# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r):
            nonlocal res
            if not r:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)
            res += abs(left) + abs(right)
            return left+right - (r.val-1)
                
        dfs(root)
        return res