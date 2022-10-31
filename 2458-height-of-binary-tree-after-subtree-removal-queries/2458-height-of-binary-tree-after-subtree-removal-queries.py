# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        @cache
        def height(r):
            return max(height(r.left), height(r.right)) + 1 if r else 0
        
        a = {}
        def dfs(r, depth, mh):
            if r:
                a[r.val] = mh
                dfs(r.left, depth+1, max(mh, depth + height(r.right)))
                dfs(r.right, depth+1, max(mh, depth + height(r.left)))
        
        dfs(root, 0, 0)
        res = []
        for q in queries:
            res.append(a[q])
        return res
            