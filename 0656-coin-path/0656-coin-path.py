class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        N = len(coins)
        dp = [inf]*N
        dp[-1] = coins[-1]
        st = deque()
        for i in range(N-1,-1,-1):
            if coins[i] == -1:
                continue
            while st and st[0] > i+maxJump:
                st.popleft()
            if st:
                dp[i] = dp[st[0]] + coins[i]
            while st and dp[st[-1]] > dp[i]:
                st.pop()
            st.append(i)
        if dp[0] == inf: return []
        res = []
        mi = dp[0]
        for i in range(N):
            if dp[i] == mi:
                res.append(i+1)
                mi -= coins[i]
        return res