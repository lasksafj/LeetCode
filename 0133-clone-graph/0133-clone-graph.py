"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node
        vis = {}
        q = deque([node])
        vis[node.val] = Node(node.val)
        while q:
            cur = q.popleft()
            ncur = vis[cur.val]
            for ne in cur.neighbors:
                if ne.val not in vis:
                    q.append(ne)
                    vis[ne.val] = Node(ne.val)
                ncur.neighbors.append(vis[ne.val])
        return vis[node.val]