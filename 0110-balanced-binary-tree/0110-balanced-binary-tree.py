# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r, d):
            if not r:
                return d
            a,b = dfs(r.left, d+1), dfs(r.right, d+1)
            if abs(a-b) > 1:
                return -inf
            return max(a,b)
        return dfs(root, 0) >= 0