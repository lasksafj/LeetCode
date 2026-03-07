class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        op = [0,0]
        for i in range(n):
            c = ord(s[i])
            op[0] += (c^i) & 1
            op[1] += (c^(~i)) & 1
        return min(op)