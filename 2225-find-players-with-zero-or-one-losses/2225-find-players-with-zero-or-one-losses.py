class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        m = defaultdict(list)
        m1 = defaultdict(list)
        for w,l in matches:
            m[l].append(w)
            m1[w].append(l)
        res1, res2 = [],[]
        for p,_ in m1.items():
            if p not in m:
                res1.append(p)
        for p,pl in m.items():
            if len(pl) == 1:
                res2.append(p)
        return [sorted(res1), sorted(res2)]