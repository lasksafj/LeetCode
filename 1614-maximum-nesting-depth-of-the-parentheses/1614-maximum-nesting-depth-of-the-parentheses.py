class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            res = max(res, depth)
        return res