# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r):
            nonlocal res
            if not r:
                return 0,0
            b = r.val
            inc_l, dec_l = 1, 1
            L = dfs(r.left)
            if r.left:
                a = r.left.val
                if a+1 == b:
                    inc_l = L[0] + 1
                if a == b+1:
                    dec_l = L[1] + 1
            inc_r, dec_r = 1, 1
            R = dfs(r.right)
            if r.right:
                a = r.right.val
                if a+1 == b:
                    inc_r = R[0] + 1
                if a == b+1:
                    dec_r = R[1] + 1
            res = max(res, inc_l + dec_r - 1, inc_r + dec_l - 1)
            return max(inc_l, inc_r), max(dec_l, dec_r)

        dfs(root)
        return res