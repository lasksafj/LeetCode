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
        m = {}
        q = deque([node])
        vis = set()
        vis.add(node.val)
        while q:
            cur = q.popleft()
            ncur = Node(cur.val)
            m[ncur.val] = (ncur,cur)
            for ne in cur.neighbors:
                if ne.val not in vis:
                    q.append(ne)
                    vis.add(ne.val)
        for v in m:
            ncur,cur = m[v]
            for ne in cur.neighbors:
                ncur.neighbors.append(m[ne.val][0])
        return m[node.val][0]