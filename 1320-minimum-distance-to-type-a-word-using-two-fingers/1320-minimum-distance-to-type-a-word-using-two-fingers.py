class Solution:
    def minimumDistance(self, word: str) -> int:
        i,j = 0,0
        mp = {}
        for c in string.ascii_uppercase:
            mp[c] = (i,j)
            j += 1
            if j == 6:
                j = 0
                i += 1
        def get_dist(i,j):
            i,j = i-1,j-1
            if i < 0 or j < 0: return 0
            a,b = mp[word[i]]
            c,d = mp[word[j]]
            return abs(a-c) + abs(b-d)
        N = len(word)
        dp = [[inf]*(N+1) for _ in range(N+1)]
        for k in range(N+1):
            dp[0][k] = dp[1][k] = 0
        for i in range(1,N+1):
            for k in range(i-1):
                dp[i][k] = min(dp[i][k], dp[i-1][k] + get_dist(i-1,i))
                dp[i][i-1] = min(dp[i][i-1], dp[i-1][k] + get_dist(k,i))
        return min(dp[i])