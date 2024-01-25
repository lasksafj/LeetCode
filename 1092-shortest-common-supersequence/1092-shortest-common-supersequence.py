class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1,str2 = str2,str1
        m,n = len(str1),len(str2)
        dp = ['']*(n+1)
        for i in range(1,m+1):
            ndp = ['']*(n+1)
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    ndp[j] = dp[j-1] + str1[i-1]
                else:                    
                    ndp[j] = ndp[j-1] if len(ndp[j-1]) > len(dp[j]) else dp[j]
            dp = ndp
        i,j = 0,0
        res = []
        for ch in dp[-1]:
            while i < len(str1) and str1[i] != ch:
                res.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != ch:
                res.append(str2[j])
                j += 1
            res.append(ch)
            i += 1
            j += 1
        res.extend(list(str1[i:]))
        res.extend(list(str2[j:]))
        return ''.join(res)