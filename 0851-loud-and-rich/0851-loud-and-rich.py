class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         dp top down is better solution

        adj = defaultdict(list)
        ind = [0]*len(quiet)
        for a,b in richer:
            adj[a].append(b)
            ind[b] += 1
        
        q = deque([i for i in range(len(ind)) if ind[i] == 0])
        res = [0]*len(quiet)
        for i in range(len(quiet)):
            res[i] = i
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for ne in adj[cur]:
                    if quiet[cur] < quiet[ne]:
                        quiet[ne] = quiet[cur]
                        res[ne] = res[cur]
                    ind[ne] -= 1
                    if ind[ne] == 0:
                        q.append(ne)

        return res