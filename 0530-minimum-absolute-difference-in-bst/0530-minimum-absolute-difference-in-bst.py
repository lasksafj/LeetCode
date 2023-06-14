# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = [inf]
        prev = [-inf]
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            res[0] = min(res[0], cur.val - prev[0])
            prev[0] = cur.val
            dfs(cur.right)
        dfs(root)
        return res[0]