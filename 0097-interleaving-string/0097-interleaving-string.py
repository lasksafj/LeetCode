class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [False] * (len(s2)+1)
        dp[-1] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1):
                    dp[j] = dp[j] & (s1[i] == s3[i+j])
                if j < len(s2) and s2[j] == s3[i+j]:
                    dp[j] |= dp[j+1]
        return dp[0]