class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1
        for n in coins:
            if n <= res:
                res += n
            else:
                return res
        return res