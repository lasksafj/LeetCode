class Solution:
    def maxLength(self, arr: List[str]) -> int:
        @cache
        def dfs(i, mask):
            if i == len(arr):
                return 0
            w = arr[i]
            res = dfs(i+1, mask)
            if len(set(w)) == len(w):
                n = 0
                for ch in w:
                    n |= 1 << (ord(ch) - ord('a'))
                if mask&n == 0:
                    res = max(res, dfs(i+1, mask|n) + len(w))
            return res
        return dfs(0, 0)