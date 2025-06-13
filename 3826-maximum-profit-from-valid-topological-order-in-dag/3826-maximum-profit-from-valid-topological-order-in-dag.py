class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        ind = [0]*n
        ind_cnt = [0]*n
        for a,b in edges:
            ind[b] |= 1<<a
            ind_cnt[b] += 1

        @cache
        def dfs(mask, deg):
            d = n - bin(mask).count('1') + 1
            res = 0
            if deg == 0:
                for a in sorted([i for i in range(n) if mask&(1<<i)], key=lambda x:score[x]):
                    res += d*score[a]
                    d += 1
                return res
            
            for i in range(n):
                if (1<<i)&mask and ind[i] & mask == 0:
                    res = max(res, dfs(mask^(1<<i), deg-ind_cnt[i]) + score[i]*d)
            return res
        mask = (1<<n) - 1
        return dfs(mask, len(edges))