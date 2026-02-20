class Solution:
    def makeLargestSpecial(self, s: str) -> str:
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