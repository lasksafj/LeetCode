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
            if not r:
                return []
            if not r.left and not r.right:
                return [1]
            A = dfs(r.left)
            B = dfs(r.right)
            res = []
            for a in A:
                for b in B:
                    if a+b <= distance:
                        ans += 1
            for a in A:
                if a < distance:
                    res.append(a+1)
            for b in B:
                if b < distance:
                    res.append(b+1)
            return res
        dfs(root)
        return ans