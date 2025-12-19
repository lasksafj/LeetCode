class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        adj[0].append([firstPerson, 0])
        secret_time = [inf]*n
        for a,b,t in meetings:
            adj[a].append([b,t])
            adj[b].append([a,t])

        res = set()
        def dfs(i,t):
            secret_time[i] = t
            for ne,nt in adj[i]:
                if secret_time[ne] > nt and t <= nt:
                    dfs(ne, nt)
        dfs(0, 0)
        return [i for i,t in enumerate(secret_time) if t < inf]