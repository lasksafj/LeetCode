class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        res = 0
        i = 1
        mp = {}
        while n > 0:
            if target-i not in mp:
                res += i
                mp[i] = 1
                n -= 1
            i += 1
        return res