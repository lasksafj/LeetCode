class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        res = 1
        a = 1
        for i in range(1, N):
            if s[i] != s[i-1]:
                a = 1
            else:
                a += 1
            res = max(res, a)
        def sol2(a,b):
            res = 0
            mp = {0: -1}
            cur = 0
            for i in range(N):
                if s[i] not in a+b:
                    mp = {0: i}
                    cur = 0
                else:
                    cur += 1 if s[i]==a else -1
                    if cur in mp:
                        res = max(res, i - mp[cur])
                    else:
                        mp[cur] = i
            return res
        res = max([res] + [sol2(a,b) for a,b in combinations('abc',2)])
        
        mp = {(0,0): -1}
        a=b=c=0
        for i in range(N):
            a += s[i] == 'a'
            b += s[i] == 'b'
            c += s[i] == 'c'
            cur = (a-b,b-c)
            if cur in mp:
                res = max(res, i - mp[cur])
            else:
                mp[cur] = i

        return res