class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        a,b = 0,0
        for c in s:
            if c == '(':
                a += 1
            elif c == ')':
                b += 1
        rev = abs(a-b)
        
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
        def dfs(i, path, k):
            if i == len(s):
                if check(path):
                    res.add(''.join(path[:]))
                return
            if k > 0 and s[i] in '()':
                dfs(i+1, path, k-1)
            path.append(s[i])
            dfs(i+1, path, k)
            path.pop()
        path = []
        for r in range(rev, len(s)+1, 2):
            res = set()
            dfs(0, path, r)
            if len(res) > 0:
                return list(res)
        return [""]
                