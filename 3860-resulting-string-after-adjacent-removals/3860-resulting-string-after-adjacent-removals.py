class Solution:
    def resultingString(self, s: str) -> str:
        A = [ord(ch) for ch in s]
        st = []
        for a in A:
            if st and abs(a-st[-1]) in [1,25]:
                st.pop()
            else:
                st.append(a)
        return ''.join(chr(a) for a in st)