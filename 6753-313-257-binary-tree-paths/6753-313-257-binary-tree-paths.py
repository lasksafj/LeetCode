# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(r, path):
            if not r:
                return
            path.append(str(r.val))
            if not r.left and not r.right:
                res.append('->'.join(path))
            dfs(r.left, path)
            dfs(r.right, path)
            path.pop()
        dfs(root, [])
        return res