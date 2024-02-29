# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        odd = 1
        while q:
            if (odd < 0 and odd*q[-1].val % 2 == 1
                or odd > 0 and odd*q[-1].val % 2 == 0):
                return False
            
            for _ in range(len(q)):
                a = q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            odd *= -1
            
            if all(odd * (q[i+1].val - q[i].val) > 0 for i in range(len(q)-1)):
                continue
            else:
                return False
        return True
                
                