class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dfs(start, aturn, M):
            if start == len(piles):
                return 0
            
            if aturn:
                res = 0
                s = 0
                for i in range(start, min(len(piles), start+2*M)):
                    s += piles[i]
                    res = max(res, dfs(i+1, aturn^1, max(M, i-start+1)) + s)
            else:
                res = 10000000000
                for i in range(start, min(len(piles), start+2*M)):
                    res = min(res, dfs(i+1, aturn^1, max(M, i-start+1)))
            
            return res
        return dfs(0, 1, 1)