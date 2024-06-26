# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        A = []
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            A.append(r.val)
            dfs(r.right)
        dfs(root)
        
        def dfs2(l,r):
            if l > r:
                return None
            mi = (l+r)//2
            return TreeNode(A[mi], dfs2(l,mi-1), dfs2(mi+1,r))
        return dfs2(0,len(A)-1)