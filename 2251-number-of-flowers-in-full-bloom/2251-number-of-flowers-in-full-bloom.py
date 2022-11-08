class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        m = defaultdict(int)
        for f in flowers:
            m[f[0]] += 1
            m[f[1]+1] -= 1
        A = []
        cur = 0
        for e in sorted(m):
            cur += m[e]
            A.append([e, cur])
        res = []
        for p in persons:
            b = bisect.bisect_left(A, [p, 1])
            if b == len(A) or A[b][0] > p:
                res.append(A[b-1][1])
            else:
                res.append(A[b][1])
        
        return res