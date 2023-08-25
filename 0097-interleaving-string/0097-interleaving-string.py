class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        @cache
        def dfs(i,j,k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1,j,k+1):
                return True
            if j < len(s2) and s2[j] == s3[k] and dfs(i,j+1,k+1):
                return True
            return False
        return dfs(0,0,0)