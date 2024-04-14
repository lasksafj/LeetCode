# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return False
            if not root.left and not root.right:
                return True
            if dfs(root.left):
                res[0] += root.left.val
            dfs(root.right)
            return False
        dfs(root)
        return res[0]