# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def dfs(r):
            nonlocal ans
            
            res = [0]*(distance+1)
            if not r:
                return res
            if not r.left and not r.right:
                res[1] = 1
                return res
            
            A = dfs(r.left)
            B = dfs(r.right)
            for i in range(1, distance):
                for j in range(1, distance):
                    if i+j <= distance:
                        ans += A[i] * B[j]
            for i in range(1, distance):
                res[i+1] += A[i] + B[i]

            return res
        dfs(root)
        return ans