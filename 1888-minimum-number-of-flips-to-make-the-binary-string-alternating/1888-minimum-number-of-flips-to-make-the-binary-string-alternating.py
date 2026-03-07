class Solution:
    def minFlips(self, s: str) -> int:
        # mask:
        # op[0]: 0101...
        # op[1]: 1010...
        n = len(s)
        op = [0,0]
        for i in range(n):
            c = ord(s[i])
            op[0] += (c^i) & 1
            op[1] += (c^(~i)) & 1
        res = min(op)
        for i in range(n):
            c = ord(s[i])
            op[0] -= (c^i) & 1
            op[0] += (c^(i+n)) & 1

            op[1] -= (c^(~i)) & 1
            op[1] += (c^(~(i+n))) & 1

            res = min(res, min(op))
        return res
