class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # define: mountain: 11.1100..00, no 1 = no 0
        # seperate s as many mountain as possible
        # define sol(s): answer function
        # s -> m1m2...mk
        # answer = sorted(sol(m1), sol(m2), ...)[::-1]
        # use cnt to determine if substring is a mountain, if 1: cnt++ else cnt--, but this can make mistake on substring like 11011000, so we cut first 1 and last 0, we run sol('1' + sub[1:-1] + '0')
        def sol(s):
            if not s: return ''
            cnt = 0
            l = 0
            A = []
            for i,c in enumerate(s):
                cnt += 1 if c == '1' else -1
                if cnt == 0:
                    A.append('1' + sol(s[l+1:i]) + '0')
                    l = i+1
            return ''.join(sorted(A, reverse=True))
        return sol(s)