class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        mp = defaultdict(int)
        for a,b in dominoes:
            if a > b:
                a,b = b,a
            res += mp[(a,b)]
            mp[(a,b)] += 1
        return res