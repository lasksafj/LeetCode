# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(r):
            if r == None:
                return 0
            if r.val >= low and r.val <= high:
                return r.val + dfs(r.left) + dfs(r.right)
            elif r.val < low:
                return dfs(r.right)
            elif r.val > high:
                return dfs(r.left)
        
        return dfs(root)