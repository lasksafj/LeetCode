# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adj = defaultdict(lambda: [0]*2)
        f = defaultdict(int)
        for p,c,l in descriptions:
            adj[p][l^1] = c
            f[c] = 1
        def dfs(i):
            if i == 0: return None
            return TreeNode(i, dfs(adj[i][0]), dfs(adj[i][1]))
        for p,c,l in descriptions:
            if f[p] == 0:
                root = p
                break
        return dfs(root)