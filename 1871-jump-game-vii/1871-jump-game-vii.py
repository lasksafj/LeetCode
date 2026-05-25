class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [0]*len(s)
        pref = [0]*(len(s)+1)
        dp[0] = 1
        for i,c in enumerate(s):
            l = max(0, i-maxJump)
            r = i-minJump
            if c == '0' and l <= r and pref[r+1]-pref[l] > 0:
                dp[i] = 1
            pref[i+1] = pref[i] + dp[i]
        return dp[-1] == 1