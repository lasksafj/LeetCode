class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                cur = leaves.popleft()
                for ne in adj[cur]:
                    adj[ne].remove(cur)
                    if len(adj[ne]) == 1:
                        leaves.append(ne)
        return leaves