class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # adj = defaultdict(list)
        # for a,b in edges:
        #     adj[a].append(b)
        #     adj[b].append(a)
        # def dfs(i,p):
        #     a,b = nums[i],nums[i]^k
        #     res = [nums[i], -inf]
        #     for ne in adj[i]:
        #         if ne == p: continue
        #         sa,sb = dfs(ne,i)
        #         na,nb = nums[ne],nums[ne]^k
        #         res = [
        #             max(res[0]+max(sa,sb), res[1]+sa-b+a-na+nb, res[1]+sb-b+a-nb+na),
        #             max(res[1]+max(sa,sb), res[0]+sa-a+b-na+nb, res[0]+sb-a+b-nb+na)
        #         ]
        #     return res
        # return max(dfs(0,-1))
        
        # tree -> not cycle -> only 1 path between 2 nodes -> can replace any 2 nodes with their xor values
        # can replace any even number of nodes with their xor values
        # dp0: xor even even number of nodes
        # dp1: xor odd odd number of nodes
        dp = [0,-inf]
        for n in nums:
            dp = [
                max(dp[0] + n, dp[1] + (n^k)),
                max(dp[0] + (n^k), dp[1] + n)
            ]
        return dp[0]