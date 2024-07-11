class Solution:
    def reverseParentheses(self, s: str) -> str:
        N = len(s)
        pair = [0] * N
        st = []
        for i in range(N):
            if s[i] == "(":
                st.append(i)
            if s[i] == ")":
                j = st.pop()
                pair[i] = j
                pair[j] = i
        d = 1
        res = ''
        i = 0
        while i < N:
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res += s[i]
            i += d
        return res