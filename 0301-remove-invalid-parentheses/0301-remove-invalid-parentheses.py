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
        def dfs(i, s, l, r):
            if l == 0 and r == 0 and check(s):
                res.append(s)
                return
            idx = i
            while idx < len(s):
                if s[idx] == '(' and l > 0:
                    dfs(idx, s[:idx] + s[idx+1:], l-1, r)
                elif s[idx] == ')' and r > 0:
                    dfs(idx, s[:idx] + s[idx+1:], l, r-1)
                while idx < len(s)-1 and s[idx] == s[idx+1]:
                    idx += 1
                idx += 1

        dfs(0, s, a, b)
        return res
                