# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
        cur = root
        prev = None
        while cur and cur.val != key:
            prev = cur
            if cur.val < key:
                cur = cur.right
            elif cur.val > key:
                cur = cur.left
            else:
                break
        if not cur:
            return root
        if not cur.left and not cur.right:
            if cur == prev.left:
                prev.left = None
            else:
                prev.right = None
            cur = None
        elif not cur.left:
            if cur == prev.left:
                prev.left = cur.right
            else:
                prev.right = cur.right
            cur = None
        elif not cur.right:
            if cur == prev.left:
                prev.left = cur.left
            else:
                prev.right = cur.left
            cur = None
        else:
            x = cur.right
            prevx = None
            while x.left:
                prevx = x
                x = x.left
            cur.val = x.val
            if prevx:
                prevx.left = x.right
                x = None
            else:
                cur.right = x.right
        return root