class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        m = defaultdict(int)
        for a,b,c in shifts:
            if c == 1:
                m[a] += 1
                m[b+1] -= 1
            else:
                m[a] -= 1
                m[b+1] += 1
        cur = 0
        s = list(s)
        for i in range(len(s)):
            if i in m:
                cur += m[i]
            s[i] = chr((ord(s[i])-ord('a') + cur) % 26 + ord('a'))
        return ''.join(s)