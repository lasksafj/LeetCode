class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return ''.join(sorted(s))
        else:
            return min(s[i:] + s[:i] for i in range(len(s)))