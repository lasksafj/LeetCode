class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        # M,N = len(robot)+1, len(factory)+1
        # dp = [[[inf]*M for _ in range(N)] for _ in range(M)]
        # for j in range(N):
        #     for k in range(M):
        #         dp[0][j][k] = 0
        # for i in range(1, M):
        #     r_p = robot[i-1]
        #     for j in range(1, N):
        #         f_p,l = factory[j-1]
        #         dp[i][j][0] = min(dp[i][j-1])
        #         for k in range(1, l+1):
        #             dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k-1] + abs(r_p-f_p) )
        # return min(dp[-1][-1])

        M,N = len(robot),len(factory)
        dp = [inf]*M
        for j in range(N):
            p,l = factory[j]
            ndp = [0]*M
            st = deque([[-1, 0]])
            pref = 0
            for i in range(M):
                pref += abs(p-robot[i])
                while st and st[0][0] < i-l:
                    st.popleft()
                while st and st[-1][-1] > dp[i]-pref:
                    st.pop()
                st.append([i, dp[i]-pref])
                ndp[i] = st[0][1] + pref
            dp = ndp
        return dp[-1]