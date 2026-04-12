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
            a,b = i//6,i%6
            c,d = j//6,j%6
            return abs(a-c) + abs(b-d)
        N = len(word)
        dp = [[inf]*26 for _ in range(N+1)]
        for k in range(26):
            dp[0][k] = dp[1][k] = 0
        for i in range(1, N+1):
            c = ord(word[i-1]) - 65
            p = ord(word[i-2]) - 65
            for k in range(26):
                dp[i][k] = min(dp[i][k], dp[i-1][k] + get_dist(p, c))
                dp[i][p] = min(dp[i][p], dp[i-1][k] + get_dist(k, c))
        return min(dp[-1])