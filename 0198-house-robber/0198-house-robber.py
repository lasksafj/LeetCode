class Solution:
    def rob(self, inputArr: List[int]) -> int:
        N = len(inputArr)
        if N == 1:
            return inputArr[0]
        dp = [inputArr[0], max(inputArr[0], inputArr[1]), 0]
        for i in range(2, N):
            dp[i%3] = max(dp[(i-1)%3], dp[(i-2)%3] + inputArr[i])
        return dp[(N-1)%3]