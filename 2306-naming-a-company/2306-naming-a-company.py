class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        m = defaultdict(set)
        for w in ideas:
            m[w[0]].add(w[1:])
        res = 0
        for a,seta in m.items():
            for b,setb in m.items():
                if a <= b:
                    continue
                res += len(seta - setb) * len(setb - seta)
        return res*2