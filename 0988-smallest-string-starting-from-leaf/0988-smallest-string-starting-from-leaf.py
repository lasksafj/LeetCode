# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = '||||'
        def dfs(cur, path):
            nonlocal res
            if not cur:
                return '|'
            
            if not cur.left and not cur.right:
                res = min(res, chr(cur.val + 97) + path)
            dfs(cur.left, chr(cur.val + 97) + path)
            dfs(cur.right, chr(cur.val + 97) + path) 

        dfs(root, '')
        return res