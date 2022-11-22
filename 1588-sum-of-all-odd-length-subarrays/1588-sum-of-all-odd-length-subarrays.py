class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0]*n
        dp_even_startat = [0]*n
        dp_odd_startat = [0]*n
        dp[0] = arr[0]
        dp_odd_startat[0] = arr[0]
        for i in range(1, n):
            noeven = (i+1)//2
            dp[i] = dp_even_startat[i-1] + arr[i]*(i+1-noeven) + dp[i-1]
            dp_even_startat[i] = dp_odd_startat[i-1] + arr[i]*noeven
            dp_odd_startat[i] = dp_even_startat[i-1] + arr[i]*(i+1-noeven)
        
        # print(dp_odd_startat)
        # print(dp_even_startat)
        return dp[-1]