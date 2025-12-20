class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for s in zip(*strs):
            if list(s) != sorted(s):
                res += 1
        return res