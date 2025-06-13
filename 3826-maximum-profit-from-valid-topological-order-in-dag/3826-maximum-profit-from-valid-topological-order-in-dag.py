class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # ind = [0]*n
        # for a,b in edges:
        #     ind[b] += 1

        # @cache
        # def dfs(mask):
        #     d = n - bin(mask).count('1') + 1
        #     res = 0
        #     for i in range(n):
        #         if (1<<i)&mask and ind[i] & mask == 0:
        #             res = max(res, dfs(mask^(1<<i)) + score[i]*d)
        #     return res
        # mask = (1<<n) - 1
        # return dfs(mask)

        N = (1<<n)-1
        ind = defaultdict(int)
        for a,b in edges:
            ind[1<<b] |= 1<<a
        A = {}
        for i in range(n):
            A[1<<i] = score[i]
        dp = [-inf] * (N+1)
        dp[N] = 0
        for mask in range(N, -1, -1):
            if dp[mask] == -inf:
                continue
            d = n - bin(mask).count('1') + 1
            tmp = mask
            while tmp:
                i = tmp&(-tmp)
                nmask = mask - i
                if ind[i] & mask == 0:
                    dp[nmask] = max(dp[nmask], dp[mask] + A[i]*d)
                tmp -= i
        return dp[0]