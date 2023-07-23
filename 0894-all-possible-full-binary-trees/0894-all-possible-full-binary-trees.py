# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n&1 == 0:
            return []
        def sol(n):
            if n == 1:
                return [TreeNode()]
            if n == 3:
                return [TreeNode(0,TreeNode(),TreeNode())]
            res = []
            for i in range(1,(n-1)//2+1,2):
                left = sol(i)
                right = sol(n-1-i)
                for l in left:
                    for r in right:
                        if i != n-1-i:
                            res.append(TreeNode(0,l,r))
                            res.append(TreeNode(0,r,l))
                        else:
                            res.append(TreeNode(0,l,r))
            return res
        return sol(n)