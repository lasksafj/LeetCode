class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        N = len(beans)
        s = sum(beans)
        res = inf
        for n in beans:
            res = min(res, s - n*N)
            N -= 1
        return res