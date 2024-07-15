# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        childs = set()
        mp = {}
        for p,c,_ in descriptions:
            if p not in mp:
                mp[p] = TreeNode(p)
            if c not in mp:
                mp[c] = TreeNode(c)
            childs.add(c)
        for p,c,isL in descriptions:
            if isL:
                mp[p].left = mp[c]
            else:
                mp[p].right = mp[c]
        for p,_,_ in descriptions:
            if p not in childs:
                return mp[p]
        return None