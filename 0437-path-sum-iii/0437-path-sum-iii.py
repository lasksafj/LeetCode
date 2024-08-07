# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        def dfs(r, mp, prev):
            nonlocal res
            if not r:
                return
            cur = prev + r.val            
            res += mp[cur-targetSum]            
            mp[cur] += 1
            dfs(r.left, mp, cur)
            dfs(r.right, mp, cur)
            mp[cur] -= 1
        mp = defaultdict(int)
        mp[0] = 1
        dfs(root, mp, 0)
        return res