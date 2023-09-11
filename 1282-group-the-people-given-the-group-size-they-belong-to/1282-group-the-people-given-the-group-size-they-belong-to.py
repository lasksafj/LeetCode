class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        N = len(groupSizes)
        m = defaultdict(list)
        res = []
        for i,sz in enumerate(groupSizes):
            m[sz].append(i)
            if len(m[sz]) == sz:
                res.append(m[sz])
                m[sz] = []
        return res