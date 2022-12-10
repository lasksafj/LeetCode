# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def summ(r):
            if r:
                return r.val + summ(r.left) + summ(r.right)
            return 0
            
        s = [summ(root)]
        res = [0]
        def dfs(r):
            if not r:
                return 0
            a = dfs(r.left)
            res[0] = max(res[0], a * (s[0] - a))
            b = dfs(r.right)
            res[0] = max(res[0], b * (s[0] - b))
            return a + b + r.val
        
        dfs(root)
        return res[0] % 1000000007