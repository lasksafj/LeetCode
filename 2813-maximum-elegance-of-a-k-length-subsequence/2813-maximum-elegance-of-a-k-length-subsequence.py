class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        A = []
        vis = set()
        res = 0
        s = 0
        for i,(a,b) in enumerate(items):
            if i < k:
                if b in vis:
                    A.append(a)
                s += a
            elif b not in vis:
                if not A:
                    break
                s -= A.pop()
                s += a
            vis.add(b)
            res = max(res, s + len(vis)**2)
        return res