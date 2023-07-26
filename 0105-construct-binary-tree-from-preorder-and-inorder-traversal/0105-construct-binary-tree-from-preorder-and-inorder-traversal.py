# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i,n in enumerate(inorder):
            m[n] = i
        i = 0
        def sol(l,r):
            if l == r:
                return None
            nonlocal i
            v = preorder[i]
            i += 1
            return TreeNode(v, sol(l, m[v]), sol(m[v]+1, r))
        return sol(0, len(inorder))