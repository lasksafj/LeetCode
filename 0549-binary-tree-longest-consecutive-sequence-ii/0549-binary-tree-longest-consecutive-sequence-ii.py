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
            inc_l, dec_l = dfs(r.left)
            inc_r, dec_r = dfs(r.right)
            if r.left and r.right:
                a = r.left.val
                b = r.val
                c = r.right.val
                if a+1 == b and b+1 == c:
                    res = max(res, inc_l + dec_r + 1)
                elif c+1 == b and b+1 == a:
                    res = max(res, inc_r + dec_l + 1)
            
            if r.left and r.left.val + 1 == r.val:
                inc_l += 1
            else:
                inc_l = 1
            if r.right and r.right.val + 1 == r.val:
                inc_r += 1
            else:
                inc_r = 1
            if r.left and r.left.val - 1 == r.val:
                dec_l += 1
            else:
                dec_l = 1
            if r.right and r.right.val - 1 == r.val:
                dec_r += 1
            else:
                dec_r = 1
            res = max(res, inc_l, dec_l, inc_r, dec_r)

            return max(inc_l, inc_r), max(dec_l, dec_r)
        
        dfs(root)
        return res