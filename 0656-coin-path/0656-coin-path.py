class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        N = len(coins)
        dp = [inf]*N
        prev = [-1]*N
        dp[0] = coins[0]
        st = deque()
        L = [1]*N
        for i in range(N):
            if coins[i] == -1:
                continue
            while st and st[0] < i-maxJump:
                st.popleft()
            if st:
                dp[i] = dp[st[0]] + coins[i]
                ma = st[0]
                for j in st:
                    if dp[j] > dp[st[0]]:
                        break
                    ma = max([ma, j], key=lambda e:[L[e], -e])
                prev[i] = ma
                L[i] = L[ma] + 1
            while st and dp[st[-1]] > dp[i]:
                st.pop()
            st.append(i)
        if dp[-1] == inf: return []
        i = N-1
        A = []
        while i != -1:
            A.append(i+1)
            i = prev[i]
        return A[::-1]