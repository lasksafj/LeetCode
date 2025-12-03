def f(a,b):
    if b == 0: return inf,inf
    if a == 0: return 0,0
    d = gcd(a,b)
    if b < 0: a,b = -a,-b
    return a//d,b//d

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        N = len(points)
        mp = defaultdict(lambda: defaultdict(int))
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                slope = f(y2-y1, x2-x1)
                if slope[0] == 0:
                    b = y2
                else:
                    b = (y2*slope[1] - slope[0]*x2) if slope[0] < inf else x2
                mp[slope][b] += 1
        res = 0
        for slope,A in mp.items():
            cur = 0
            p = 0
            for v in A.values():
                cur += p*v
                p += v
            res += cur
        mid_cnt = defaultdict(lambda: defaultdict(int))
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                mid = (x1+x2, y1+y2)
                slope = f(y2-y1, x2-x1)
                mid_cnt[mid][slope] += 1
        for A in mid_cnt.values():
            cur = 0
            p = 0
            for v in A.values():
                cur += p*v
                p += v
            res -= cur
        return res