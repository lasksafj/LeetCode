class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = set()
        for i in range(len(s)-k+1):
            a.add(int(s[i:i+k], 2))
        return len(a) == 1<<k