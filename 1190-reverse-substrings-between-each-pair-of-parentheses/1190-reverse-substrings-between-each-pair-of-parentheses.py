class Solution:
    def reverseParentheses(self, s: str) -> str:
        def dfs(i, d):
            res = ''
            fin_left = False
            j = i
            while j < len(s) and s[j] != ')':
                if s[j] != '(':
                    res += s[j]
                else:
                    ret, r = dfs(j+1, 1)
                    res += ret
                    j = r+1

                j += 1
            if d:
                res = res[::-1]
            return (res, j-1)
        return dfs(0, 0)[0]