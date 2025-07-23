class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        parent = [-1]*len(nums)
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        @cache
        def dfs(i, d, odd):
            no_flip = -nums[i] if odd else nums[i]
            flip = -no_flip
            for ne in adj[i]:
                if ne == parent[i]:
                    continue
                parent[ne] = i
                no_flip += dfs(ne, min(k, d+1), odd)
                if d == k:
                    flip += dfs(ne, 1, odd^1)
            if d == k:
                return max(no_flip, flip)
            return no_flip
        return dfs(0, k, 0)