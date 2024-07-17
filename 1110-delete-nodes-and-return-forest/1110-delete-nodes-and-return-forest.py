# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        if root.val not in to_delete:
            res = [root]
        def dfs(r):
            if not r:
                return None
            r.left = dfs(r.left)
            r.right = dfs(r.right)
            if r.val in to_delete:
                if r.left:
                    res.append(r.left)
                if r.right:
                    res.append(r.right)
                return None
            return r
        dfs(root)
        return res