class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pre = [0]*(N+1)
        for i in range(N):
            pre[i+1] = pre[i] + nums[i]
        def cal_sum(a,b):
            return pre[b] - pre[a]

        dp1 = [[-1]*(k+1) for _ in range(N+1)]
        dp2 = [[-inf]*(k+1) for _ in range(N+1)]
        for i in range(N+1):
            dp2[i][0] = 0
        for i in range(N-1,-1,-1):
            for j in range(1,min(k, N-i)+1):
                b = dp1[i+1][j]
                ans1 = nums[i]*j* pow(-1, ((j-1)%2) ) + dp2[i+1][j-1]
                if b == -1:
                    ans2 = -inf
                else:
                    ans2 = cal_sum(i,b)*j*(-1)**((j-1)%2) + dp2[b][j-1]
                if ans1 >= ans2:
                    bb = i+1
                    dp2[i][j] = max(dp2[i+1][j] , ans1)
                else:
                    bb = b
                    dp2[i][j] = max(dp2[i+1][j] , ans2)
                dp1[i][j] = bb
        return dp2[0][k]