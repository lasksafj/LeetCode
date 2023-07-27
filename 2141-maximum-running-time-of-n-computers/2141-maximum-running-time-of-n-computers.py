class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        k = 1
        res = batteries[-n]
        for i in range(len(batteries)-n, len(batteries)-1):
            diff = batteries[i+1] - batteries[i]
            if extra > diff*k:
                extra -= diff*k
                res = batteries[i+1]
            else:
                return res + extra//k
            k += 1
        return res + extra//n