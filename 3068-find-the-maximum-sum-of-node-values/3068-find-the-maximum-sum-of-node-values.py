class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(prev,i):
            # dpa: i not xor k, dpb: i xor k
            dpa,dpb = nums[i],-inf
            for ne in adj[i]:
                if ne != prev:
                    # a: ne not xor k, b: ne xor k
                    a,b = dfs(i,ne)
                    # not xor edge
                    n_dpa = max(a,b) + dpa
                    n_dpb = max(a,b) + dpb
                    # xor edge
                    n_dpa = max(n_dpa, 
                                dpb-(nums[i]^k)+nums[i] + a-nums[ne]+(nums[ne]^k), 
                                dpb-(nums[i]^k)+nums[i] + b-(nums[ne]^k)+nums[ne])
                    n_dpb = max(n_dpb, 
                                dpa+(nums[i]^k)-nums[i] + a-nums[ne]+(nums[ne]^k), 
                                dpa+(nums[i]^k)-nums[i] + b-(nums[ne]^k)+nums[ne])
                    dpa,dpb = n_dpa,n_dpb
            if len(adj[i]) == 1 and prev != -1:
                return nums[i],-inf
            return dpa,dpb
        return max(dfs(-1,0))