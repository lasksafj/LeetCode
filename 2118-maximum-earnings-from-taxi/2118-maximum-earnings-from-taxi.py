class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides = [[0,0,0]] + rides
        rides.sort(key=lambda x:x[1])
        dp = [0]*len(rides)
        for i in range(1, len(rides)):
            a,b,c = rides[i]
            j = bisect_right(rides, a, key=lambda x:x[1]) - 1
            dp[i] = max(dp[i-1], dp[j] + b-a+c)
        return dp[-1]