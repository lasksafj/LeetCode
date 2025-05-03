class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # dp0[i]: max size of subarr end at i, last comparison <
        # dp1[i]: max size of subarr end at i, last comparison >
        dp = [0,0]
        res = 0
        prev = arr[0]
        for n in arr:
            if prev < n:
                dp = [
                    1,
                    dp[0] + 1
                ]
            elif prev > n:
                dp = [
                    dp[1] + 1,
                    1
                ]
            else:
                dp = [1,1]
            res = max(res, max(dp))
            prev = n
        return res