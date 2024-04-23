class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaf_list = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaf_list.append(i)
        
        while n > 2:
            n_leaf_list = []
            for leaf in leaf_list:
                ne = next(iter(adj[leaf]))
                adj[ne].remove(leaf)
                if len(adj[ne]) == 1:
                    n_leaf_list.append(ne)
            n -= len(leaf_list)
            leaf_list = n_leaf_list
        return leaf_list