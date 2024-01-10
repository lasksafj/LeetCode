# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def dfs(r):
            if r.left:
                adj[r.val].append(r.left.val)
                adj[r.left.val].append(r.val)
                dfs(r.left)
            if r.right:
                adj[r.val].append(r.right.val)
                adj[r.right.val].append(r.val)
                dfs(r.right)
        dfs(root)
        q = deque([start])
        res = 0
        vis = set()
        vis.add(start)
        while q:
            for _ in range(len(q)):
                for ne in adj[q.popleft()]:
                    if ne not in vis:
                        q.append(ne)
                        vis.add(ne)
            res += 1
        return res-1