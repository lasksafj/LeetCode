class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = [defaultdict(int) for _ in range(len(words[0]))]
        for j in range(len(words[0])):
            for i in range(len(words)):
                m[j][words[i][j]] += 1
        dp = [[0]*len(target) for _ in range(len(words[0])+1)]
        for j in range(len(words[0])):
            r = j+1
            dp[r][0] = dp[r-1][0] + m[j][target[0]]
            for i in range(1, len(target)):
                dp[r][i] = dp[r-1][i-1] * m[j][target[i]] + dp[r-1][i]
        # print(dp)
        return dp[len(words[0])][len(target)-1] % 1000000007