class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        m = set()
        for a,_ in paths:
            m.add(a)
        for _,b in paths:
            if b not in m:
                return b
        return ''