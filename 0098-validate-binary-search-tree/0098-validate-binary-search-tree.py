# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def sol(root, l, r):
            if not root:
                return True
            if l < root.val < r:
                return sol(root.left, l, root.val) and sol(root.right, root.val, r)
            return False
        return sol(root, -inf, inf)