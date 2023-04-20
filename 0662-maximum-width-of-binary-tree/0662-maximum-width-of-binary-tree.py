# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,1)])
        res = 0
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                c,p = q.popleft()
                if c.left:
                    q.append((c.left,p*2))
                if c.right:
                    q.append((c.right,p*2+1))
        return res
            