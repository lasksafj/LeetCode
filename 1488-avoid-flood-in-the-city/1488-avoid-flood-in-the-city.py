from sortedcontainers import SortedSet
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        fill_date = {}
        dry = SortedSet()
        res = [1]*N
        for i,city in enumerate(rains):
            if city > 0:
                res[i] = -1
                if city in fill_date:
                    p = dry.bisect_right(fill_date[city])
                    if p == len(dry):
                        return []
                    res[dry[p]] = city
                    dry.pop(p)
                    fill_date[city] = i
                else:
                    fill_date[city] = i
            else:
                dry.add(i)
        return res