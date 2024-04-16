# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def sol(cur, depth):
            if not cur:
                return None
            if depth == 0:
                cur.left = TreeNode(val, cur.left, None)
                cur.right = TreeNode(val, None, cur.right)
            sol(cur.left, depth-1)
            sol(cur.right, depth-1)
            return cur
        if depth == 1:
            return TreeNode(val, root, None)
        return sol(root, depth-2)