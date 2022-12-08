# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(r, A):
            if not r.left and not r.right:
                A.append(r.val)
                return
            if r.left:
                dfs(r.left, A)
            if r.right:
                dfs(r.right, A)
        a1 = []
        a2 = []
        dfs(root1, a1)
        dfs(root2, a2)
        return a1 == a2