class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for n in arr1:
            cur = trie
            for ch in str(n):
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
        res = 0
        for n in arr2:
            cur = trie
            l = 0
            for ch in str(n):
                if ch in cur:
                    cur = cur[ch]
                    l += 1
                else:
                    break
            res = max(res, l)
        return res