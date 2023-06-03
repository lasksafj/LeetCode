class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def getCount(s):
            l, r = 0, 0
            for c in s:
                if c == "(": l+=1
                elif c == ")":
                    if l == 0:
                        r += 1
                    else: l-=1
            return l, r

        def val(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count-=1
                if count<0:
                    return False
            return True

        ans = []

        def dfs(s, ind, l, r):
            if l == 0 and r == 0 and val(s):
                ans.append(s)
                return
            for i in range(ind, len(s)):
                if i > ind and s[i] == s[i-1]:
                    continue
                if r > 0 and s[i] == ")":
                    dfs(s[:i] + s[i+1:], i, l, r-1)
                elif l > 0 and s[i] == "(":
                    dfs(s[:i] + s[i+1:], i, l-1, r)
        
        l, r = getCount(s)
        dfs(s, 0, l, r)
        return ans