# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return None
            if cur.val > key:
                cur.left = dfs(cur.left)
            elif cur.val < key:
                cur.right = dfs(cur.right)
            else:
                if not cur.left:
                    return cur.right
                elif not cur.right:
                    return cur.left
                else:
                    x = cur.right
                    prevx = None
                    while x.left:
                        prevx = x
                        x = x.left
                    cur.val = x.val
                    if prevx:
                        prevx.left = x.right
                    else:
                        cur.right = x.right
            return cur
        return dfs(root)