# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 1
        l = 0
        s = -inf
        while q:
            l += 1
            cur = 0
            for _ in range(len(q)):
                u = q.popleft()
                cur += u.val
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            if cur > s:
                res = l
                s = cur
        return res