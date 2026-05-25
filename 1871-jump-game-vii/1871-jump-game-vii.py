class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        dp = [False]*N
        dp[0] = True
        r = 0
        for i,c in enumerate(s):
            if not dp[i]: continue
            r = max(r, i+1)
            for j in range(max(r, i+minJump), min(N, i+maxJump+1)):
                if s[j] == '0':
                    dp[j] = True
            r = max(r, i+maxJump)
        return dp[-1]