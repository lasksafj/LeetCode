class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        @cache
        def dfs(i):
            if i >= N:
                return 0
            return dfs(i+k) + energy[i]
        return max(dfs(i) for i in range(N))