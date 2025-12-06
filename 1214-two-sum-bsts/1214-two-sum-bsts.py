# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(r, A):
            if not r: return
            A.add(r.val)
            dfs(r.left, A)
            dfs(r.right, A)
        A,B = set(),set()
        dfs(root1, A)
        dfs(root2, B)
        return any(target-b in A for b in B)