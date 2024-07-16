# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(r):
            if not r or r.val == startValue or r.val == destValue:
                return r
            left,right = lca(r.left),lca(r.right)
            return r if left and right else left or right
        r = lca(root)
        sp,dp = '', ''
        q = deque([[r, '']])
        while q and (sp == '' or dp == ''):
            r,p = q.popleft()
            if r.val == startValue:
                sp = p
            if r.val == destValue:
                dp = p
            if r.left:
                q.append([r.left, p+'L'])
            if r.right:
                q.append([r.right, p+'R'])
        return 'U'*len(sp) + dp