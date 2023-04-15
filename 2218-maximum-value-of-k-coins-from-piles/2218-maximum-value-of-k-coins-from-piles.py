class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prev = [0]
        for i in range(len(piles)):
            s = len(piles[i])
            l = len(prev)
            # prefix_sum[i] = sum(pile[:i])
            prefix_sum = [0] * (s + 1)
            for j in range(s):
                prefix_sum[j + 1] = prefix_sum[j] + piles[i][j]
            max_size = s + l
            dp = [0] * min(k + 1, max_size)
            for j in range(len(dp) - 1, -1, -1):
                temp = 0
                for q in range(max(0, j - l + 1), min(s ,j) + 1):
                    temp = max(temp, prev[j - q] + prefix_sum[q])
                dp[j] = temp
            prev = dp
        return dp[k]