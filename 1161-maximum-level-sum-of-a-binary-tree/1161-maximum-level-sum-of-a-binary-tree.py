# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        cur_s = -inf
        res = 1
        level = 0
        while q:
            s = 0
            level += 1
            for _ in range(len(q)):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                s += c.val
            if s > cur_s:
                res = level
                cur_s = s
        return res