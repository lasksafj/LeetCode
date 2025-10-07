class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        res = [-1]*N
        A = SortedList()
        last_idx = {}
        for i,r in enumerate(rains):
            if r > 0:
                if r in last_idx:
                    j = A.bisect_left(last_idx[r])
                    if j == len(A):
                        return []
                    res[A[j]] = r
                    A.pop(j)
                last_idx[r] = i
            else:
                A.add(i)
        for i in range(N):
            if rains[i] == 0 and res[i] == -1:
                res[i] = 1
        return res