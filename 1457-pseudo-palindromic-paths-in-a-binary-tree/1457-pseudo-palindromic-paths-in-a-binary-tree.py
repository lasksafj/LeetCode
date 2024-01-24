# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(cur, mask):
            if not cur:
                return 0
            mask ^= (1<<cur.val)
            if not cur.left and not cur.right:
                return int(mask&(mask-1) == 0)
            return dfs(cur.left, mask) + dfs(cur.right, mask)
        return dfs(root, 0)