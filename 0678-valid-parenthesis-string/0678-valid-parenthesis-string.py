class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        l,r = 0,0
        for i in range(N):
            if s[i] == '(' or s[i] == '*':
                l += 1
            else:
                l -= 1
            if s[N-i-1] == ')' or s[N-i-1] == '*':
                r += 1
            else:
                r -= 1
            if l < 0 or r < 0:
                return False
        return True