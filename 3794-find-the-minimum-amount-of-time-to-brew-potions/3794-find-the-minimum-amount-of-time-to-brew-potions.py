class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        N = len(skill)
        pre = list(accumulate(skill, initial=0))
        tb = pre[-1]*mana[0]
        ta = 0
        prev_m = mana[0]
        for m in mana[1:]:
            t = tb
            for i in range(N-2,-1,-1):
                t = max(t - m*skill[i], ta + pre[i+1]*prev_m)
            tb = t + pre[-1]*m
            ta = t
            prev_m = m
        return tb