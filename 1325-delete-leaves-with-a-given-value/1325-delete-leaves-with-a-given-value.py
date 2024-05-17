# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(r):
            if not r:
                return r
            if not r.left and not r.right:
                if r.val == target:
                    return None
                return r
            r.left = dfs(r.left)
            r.right = dfs(r.right)
            
            if not r.left and not r.right:
                if r.val == target:
                    return None
                return r
            return r
        return dfs(root)