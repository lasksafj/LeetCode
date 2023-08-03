class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        N = len(stones)
        if (N-k)%(k-1) != 0:
            return -1
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + stones[i]
        
        # the cost needed to merge stone[i] ~ stones[j] into m piles.
        @cache
        def dfs(i,j,m):
            if (j-i+1-m) % (k-1) != 0:
                return inf
            if i == j:
                if m == 1:
                    return 0
                return inf
            if m == 1:
                return dfs(i, j, k) + prefix[j + 1] - prefix[i]
            return min(dfs(i,mid,1) + dfs(mid+1,j,m-1) for mid in range(i, j))
        return dfs(0,N-1,1)