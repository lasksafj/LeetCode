# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        ans = ''
        def dfs(r):
            nonlocal ans
            res = ['',0]
            if not r:
                return res
            if r.val == startValue:
                res = ['', 1]
            elif r.val == destValue:
                res = ['', 2]
            
            a = dfs(r.left)
            b = dfs(r.right)
            
            
            if a[1] == 1 and b[1] == 2:
                ans = a[0]+'U' + 'R'+b[0]
            elif a[1] == 2 and b[1] == 1:
                ans = b[0]+'U' + 'L'+a[0]
            elif a[1] == 1:
                if res[1] == 2:
                    ans = a[0]+'U'
                else:
                    res = [a[0]+'U', 1]
            elif a[1] == 2:
                if res[1] == 1:
                    ans = 'L'+a[0]
                else:
                    res = ['L'+a[0], 2]
            elif b[1] == 1:
                if res[1] == 2:
                    ans = b[0]+'U'
                else:
                    res = [b[0]+'U', 1]
            elif b[1] == 2:
                if res[1] == 1:
                    ans = 'R'+b[0]
                else:
                    res = ['R'+b[0], 2]
            # print(r.val,a,b,res)
            return res
        dfs(root)
        return ans