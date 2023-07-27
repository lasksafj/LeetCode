class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        def check(x):
            s = sum(batteries[:-n])
            for b in batteries[-n:]:
                if b < x:
                    s -= (x-b)
                    if s < 0:
                        return False
            return True
        # print(check(12))
        l,r = 1, sum(batteries)
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                l = mi+1
            else:
                r = mi-1
        return r