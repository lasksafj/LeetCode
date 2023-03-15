# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        stop = False
        while q:
            c = q.popleft()
            if not c:
                stop = True
            else:
                if stop:
                    return False
                q.append(c.left)
                q.append(c.right)
        return True
            
                    