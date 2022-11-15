# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def check(x):
            a = 1
            while x > 1:
                a = (a<<1) | (x&1)
                x >>= 1
            r = root
            while a > 1:
                if a&1:
                    r = r.right
                else:
                    r = r.left
                a >>= 1
            return r != None
        
        cnt = 1
        r = root
        while r.right:
            r = r.right
            cnt += 1
        l = 2**cnt-1
        r = l*2
        n = l
        a = 1 << cnt
        # print(check(0|a),check(1|a),check(2|a),check(3|a))
        while l < r:
            m = (l+r)//2
            if m == l:
                break
            if check((m-n-1)|a):
                l = m
            else:
                r = m-1
        return r if check(r) else l
            