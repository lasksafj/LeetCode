class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i%2 and s[i] == '0':
                res += 1
            elif i%2 == 0 and s[i] == '1':
                res += 1
        return min(res, len(s)-res)