# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(r):
            if not r or r == p or r == q:
                return r
            left,right = dfs(r.left),dfs(r.right)
            return r if left and right else left or right
        return dfs(root)