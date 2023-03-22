# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i,n in enumerate(postorder):
            m[n] = i
        idx = [-1]
        def sol(l,r):
            if l > r:
                return None
            idx[0] += 1
            i = idx[0]
            v = preorder[i]
            if i+1 < len(preorder):
                mi = m[preorder[i+1]]
            else:
                mi = r-1
            lt = sol(l, min(mi, r-1))
            rt = sol(max(l, mi + 1), r-1)
            return TreeNode(v, lt, rt)
        return sol(0, len(postorder)-1)