# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return 0,0
            _, r = dfs(root.left)
            res_l = r+1
            l,_ = dfs(root.right)
            res_r = l+1    
            res[0] = max(res[0], res_l, res_r)
            return res_l, res_r
        dfs(root)
        return res[0]-1