class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        N = len(robots)
        walls.sort()
        RD = [[-inf, 0]] + sorted(list(zip(robots, distance)), key=lambda x: x[0]) + [[inf,0]]
        dp = [[0]*2 for _ in range(len(RD))]
        for i in range(1, N+1):
            p, d = RD[i]
            lp, ld = RD[i-1]

            a = max(lp+1, p-d)
            k = bisect_right(walls, p) - bisect_left(walls, a)
            dp[i][0] = dp[i-1][0] + k
            a = max(lp+ld+1, p-d)
            k = bisect_right(walls, p) - bisect_left(walls, a)
            dp[i][0] = max(dp[i][0], dp[i-1][1] + k)

            rp,rd = RD[i+1]
            b = min(p+d, rp-1)
            k = bisect_right(walls, b) - bisect_left(walls, p)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + k
            
        return max(dp[-2])