class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ch1,ch2 = 'a','b'
        if x < y:
            ch1 = 'b'
            ch2 = 'a'
            x,y = y,x
        res = 0
        st = []
        for ch in s+'-':
            if ch == ch1:
                st.append(ch1)
            elif ch == ch2:
                if st and st[-1] == ch1:
                    st.pop()
                    res += x
                else:
                    st.append(ch2)
            else:
                cnt = Counter(st)
                if len(cnt) == 2:
                    res += min(cnt.values()) * y
                st = []
        return res
                