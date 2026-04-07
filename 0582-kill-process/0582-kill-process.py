class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        res = []
        adj = defaultdict(list)
        for a,b in zip(pid,ppid):
            adj[b].append(a)
        def dfs(i):
            res.append(i)
            for ne in adj[i]:
                dfs(ne)
        dfs(kill)
        return res