class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        N = len(target)
        mp = [{} for _ in range(max(len(w) for w in words) + 1)]
        for w, c in zip(words, costs):
            if w not in mp[len(w)] or mp[len(w)][w] > c:
                mp[len(w)][w] = c
            
        lengths = [l for l in range(len(mp)) if len(mp[l]) > 0]
        dp = [inf] * (N + 1)
        dp[0] = 0
        for i in range(N): 
            for j in lengths:
                if i+j > N:
                    break
                try:
                    cost = mp[j][target[i:i+j]]
                    if cost + dp[i] < dp[i+j]:
                        dp[i+j] = cost + dp[i]
                except:
                    pass
        return dp[N] if dp[N] < inf else -1