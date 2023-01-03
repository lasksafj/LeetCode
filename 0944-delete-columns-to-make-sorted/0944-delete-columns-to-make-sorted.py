class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        n = len(strs[0])
        for i in range(n):
            a = 'a'
            for s in strs:
                if s[i] < a:
                    res += 1
                    break
                a = s[i]
        return res