class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        res = 0
        for n in target:
            res += max(0, n-prev)
            prev = n
        return res