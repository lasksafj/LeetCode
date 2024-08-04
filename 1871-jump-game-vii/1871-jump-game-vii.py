class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        res = [0]*N
        res[0] = 1
        j = 0
        for i in range(N):
            if s[i] == '1' or res[i] == 0:
                continue
            l,r = i+minJump,i+maxJump
            j = max(j, l)
            while j <= min(r,N-1):
                if s[j] == '0':
                    res[j] = 1
                j += 1
        return res[-1]