# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def build(prev,cur):
            if not cur:
                return
            if prev:
                adj[prev].append(cur)
                adj[cur].append(prev)
            build(cur,cur.left)
            build(cur,cur.right)
        build(None, root)
        res = []
        def dfs(prev,cur,k,res):
            if not cur:
                return
            if k == 0:
                res.append(cur.val)
            for ne in adj[cur]:
                if ne != prev:
                    dfs(cur,ne,k-1,res)
        dfs(None, target, k, res)
        return res