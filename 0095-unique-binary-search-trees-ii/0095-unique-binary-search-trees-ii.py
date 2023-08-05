# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def sol(l,r):
            if l > r:
                return [None]
            res = []
            for i in range(l,r+1):
                left_arr = sol(l,i-1)
                right_arr = sol(i+1,r)
                for left in left_arr:
                    for right in right_arr:
                        res.append(TreeNode(i, left, right))
            return res
        return sol(1,n)