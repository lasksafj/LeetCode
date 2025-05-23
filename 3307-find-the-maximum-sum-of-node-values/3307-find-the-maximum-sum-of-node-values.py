class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i,p):
            a,b = nums[i],nums[i]^k
            res = [nums[i], -inf]
            for ne in adj[i]:
                if ne == p: continue
                sa,sb = dfs(ne,i)
                na,nb = nums[ne],nums[ne]^k
                res = [
                    max(res[0]+max(sa,sb), res[1]+sa-b+a-na+nb, res[1]+sb-b+a-nb+na),
                    max(res[1]+max(sa,sb), res[0]+sa-a+b-na+nb, res[0]+sb-a+b-nb+na)
                ]
            return res
        return max(dfs(0,-1))