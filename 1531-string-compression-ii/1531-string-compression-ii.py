class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dfs(i,k,prev_ch,prev_n):
            # print(i,k,prev_ch,prev_n)
            if i == len(s):
                return 0
            
            ch = s[i]
            if prev_ch == ch:
                n = prev_n+1
                if (n > 0 and pow(10, int(log(n,10))) == n ) or n == 2:
                    d = 1
                else:
                    d = 0
                a = dfs(i+1,k,ch,n) + d
            else:
                n = 1
                a = dfs(i+1,k,ch,n) + 1
                
            b = dfs(i+1, k-1, prev_ch, prev_n) if k > 0 else inf
            return min(a,b)
        return dfs(0,k,'-',0)