class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1,str2 = str2,str1
        m,n = len(str1),len(str2)
        dp = [0]*(n+1)
        mp = defaultdict(lambda:[-1,-1,None])
        for i in range(1,m+1):
            ndp = [0]*(n+1)
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    ndp[j] = dp[j-1] + 1
                    mp[(i,j)] = [i-1,j-1, mp[(i-1,j-1)]]
                else:
                    ma = max(ndp[j-1], dp[j])
                    ndp[j] = ma
                    if ma == ndp[j-1]:
                        mp[(i,j)] = mp[(i,j-1)]
                    else:
                        mp[(i,j)] = mp[(i-1,j)]
            dp = ndp
        # print(dp)
        # print(mp)
        A = []
        cur = mp[(m,n)]
        # print(ch,i,j)
        while cur:
            i,j,cur = cur
            A.append([i,j])

        # print(A[::-1][1:])
        res = ''
        prei,prej = 0,0
        for i,j in A[::-1][1:]:
            res += str1[prei:i] + str2[prej:j] + str1[i]
            prei,prej = i+1,j+1
            # print(res)
        res += str1[prei:] + str2[prej:]
        return res