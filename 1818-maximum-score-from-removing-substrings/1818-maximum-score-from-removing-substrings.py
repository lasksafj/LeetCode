class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        rev = 'ab'
        if x < y:
            rev = 'ba'
            x,y = y,x
        N = len(s)
        st = []
        res = 0
        for i in range(N):
            if st and st[-1] == rev[0] and s[i] == rev[1]:
                st.pop()
                res += x
            else:
                st.append(s[i])
        s = st[:]
        st = []
        rev = rev[::-1]
        x = y
        for i in range(len(s)):
            if st and st[-1] == rev[0] and s[i] == rev[1]:
                st.pop()
                res += x
            else:
                st.append(s[i])
        return res