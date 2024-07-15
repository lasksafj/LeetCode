class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre = list(accumulate(stones))
        # print(pre)
        @cache
        def dfs(i, a):
            if i == len(stones)-1:
                return pre[i] if a else -pre[i]
            if a:
                return max( dfs(i+1, a), dfs(i+1, a^1) + pre[i])
            else:
                return min( dfs(i+1, a), dfs(i+1, a^1) - pre[i])
        return dfs(1,1)