# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i = [len(postorder)-1]
        m = {}
        for a,b in enumerate(inorder):
            m[b] = a
        def sol(l,r):
            if l > r:
                return None
            v = postorder[i[0]]
            i[0] -= 1
            if l == r:
                return TreeNode(v, None, None)
            rtree = sol(m[v]+1, r)
            ltree = sol(l,m[v]-1)
            return TreeNode(v, ltree, rtree)
        return sol(0, len(inorder)-1)