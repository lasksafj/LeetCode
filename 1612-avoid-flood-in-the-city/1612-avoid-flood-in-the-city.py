class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        res = [-1]*N
        next_zero = [-1]*N
        k = N
        zeros = set()
        for i in range(N-1,-1,-1):
            next_zero[i] = k
            if rains[i] == 0:
                k = i
                zeros.add(i)
        def find(i):
            res = next_zero[i]
            if res == N:
                return N
            if next_zero[i] not in zeros:
                res = find(next_zero[i])
            next_zero[i] = res
            return res
        
        last_idx = {}
        for i,r in enumerate(rains):
            if r > 0:
                if r in last_idx:
                    j = find(last_idx[r])
                    if j > i:
                        return []
                    res[j] = r
                    zeros.remove(j)
                last_idx[r] = i

        for i in range(N):
            if rains[i] == 0 and res[i] == -1:
                res[i] = 1
        return res