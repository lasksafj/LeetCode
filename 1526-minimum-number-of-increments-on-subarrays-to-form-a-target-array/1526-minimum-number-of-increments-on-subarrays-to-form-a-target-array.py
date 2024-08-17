class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        res = 0
        for n in target[::-1]:
            if n > prev:
                res += n-prev
            prev = n
        return res