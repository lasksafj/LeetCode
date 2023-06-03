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
        
        res = set()
        def dfs(i, path, l, r):
            if i == len(s):
                if l == 0 and r == 0 and check(path):
                    res.add(''.join(path[:]))
                return
            if s[i] == '(' and l > 0:
                dfs(i+1, path, l-1, r)
            if s[i] == ')' and r > 0:
                dfs(i+1, path, l, r-1)
            path.append(s[i])
            dfs(i+1, path, l, r)
            path.pop()
        path = []
        dfs(0, path, a, b)
        return res
                