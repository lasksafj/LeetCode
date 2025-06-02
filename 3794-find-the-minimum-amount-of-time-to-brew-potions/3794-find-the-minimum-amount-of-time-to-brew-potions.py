class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        N = len(skill)
        time = [0]*N
        for m in mana:
            a = 0
            ntime = [0]*N
            for i,k in enumerate(skill):
                a = max(a, time[i])
                a += k*m
                ntime[i] = a
            time[-1] = ntime[-1]
            for i in range(N-2, -1, -1):
                time[i] = time[i+1] - m*skill[i+1]
        return time[-1]