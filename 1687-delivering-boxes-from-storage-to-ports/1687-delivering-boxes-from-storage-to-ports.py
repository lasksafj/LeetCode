class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        N = len(boxes)
        dp = [0] + [inf]*N
        trip = 0
        prev_j = 0
        j = 0
        for i in range(N):
            while j < N and maxBoxes > 0 and maxWeight >= boxes[j][1]:
                maxBoxes -= 1
                maxWeight -= boxes[j][1]
                if j == 0 or boxes[j][0] != boxes[j-1][0]:
                    trip += 1
                    prev_j = j
                j += 1
            
            dp[j] = min(dp[j], dp[i] + trip + 1)
            dp[prev_j] = min(dp[prev_j], dp[i] + trip)
            
            maxBoxes += 1
            maxWeight += boxes[i][1]
            if i < N-1 and boxes[i][0] != boxes[i+1][0]:
                trip -= 1
        return dp[-1]