class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        a,b = 0,0
        for c in s:
            if c == '(':
                a += 1
            elif c == ')':
                if a == 0:
                    b += 1
                else:
                    a -= 1
        
        def check(path):
            st = []
            for c in path:
                if c.isalpha():
                    continue
                if c == '(':
                    st.append(c)
                else:
                    if st:
                        st.pop()
                    else:
                        return False
            return len(st) == 0
        
        res = []
        def dfs(s, ind, l, r):
            if l == 0 and r == 0 and check(s):
                res.append(s)
                return
            for i in range(ind, len(s)):
                if i > ind and s[i] == s[i-1]:
                    continue
                if r > 0 and s[i] == ")":
                    dfs(s[:i] + s[i+1:], i, l, r-1)
                elif l > 0 and s[i] == "(":
                    dfs(s[:i] + s[i+1:], i, l-1, r)
        path = []
        dfs(s, 0, a, b)
        return res
                