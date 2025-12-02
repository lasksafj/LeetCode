class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mp = defaultdict(int)
        for x,y in points:
            mp[y] += 1
        A = []
        for a in mp.values():
            A.append(comb(a,2))
        t = 0
        res = 0
        for a in A:
            res += a*t
            t += a
        return res % (10**9+7)