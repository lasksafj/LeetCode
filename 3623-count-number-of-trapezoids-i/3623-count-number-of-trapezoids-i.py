class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mp = defaultdict(int)
        for x,y in points:
            mp[y] += 1
        t = res = 0
        for a in mp.values():
            n_edges = a*(a-1)//2
            res += n_edges * t
            t += n_edges
        return res % (10**9+7)