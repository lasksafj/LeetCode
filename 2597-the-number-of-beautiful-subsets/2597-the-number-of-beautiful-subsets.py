class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        m = [defaultdict(int) for _ in range(k)]
        for n in nums:
            m[n%k][n] += 1
        res = 1
        for i in range(k):
            dp0,dp1,prev = 1,0,0    #dp0 number of subsets not pick cur, dp1 number of subsets pick cur, prev previous number of cur in arr
            for cur in sorted(m[i]):
                v = pow(2, m[i][cur]) - 1 #number of subsets contain only cur, not include empty subset
                if cur-k == prev:
                    dp0,dp1 = dp0+dp1, dp0*v
                else:
                    dp0,dp1 = dp0+dp1, (dp0+dp1)*v
                prev = cur
            res *= (dp0+dp1)
        return res-1