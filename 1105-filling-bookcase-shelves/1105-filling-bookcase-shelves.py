class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        dp = [inf] * (N+1)
        dp[0] = 0
        for i in range(N):
            ma = 0
            w = 0
            for j in range(i,-1,-1):
                ma = max(ma, books[j][1])
                if w+books[j][0] <= shelfWidth:
                    dp[i+1] = min(dp[i+1], dp[j] + ma)
                    w += books[j][0]
                else:
                    break
        # print(dp)
        return dp[-1]