class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        T = {}
        for a in arr1:
            a = str(a)
            t = T
            for c in a:
                if c not in t:
                    t[c] = {}
                t = t[c]
        res = 0
        for a in arr2:
            a = str(a)
            t = T
            l = 0
            for c in a:
                if c not in t:
                    break
                t = t[c]
                l += 1
            res = max(res, l)
        return res