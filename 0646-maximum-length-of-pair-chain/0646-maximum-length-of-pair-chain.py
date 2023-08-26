class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:(x[1], -x[0]))
        # print(pairs)
        res = 0
        r = -inf
        for a,b in pairs:
            if a > r:
                res += 1
                r = b
        return res