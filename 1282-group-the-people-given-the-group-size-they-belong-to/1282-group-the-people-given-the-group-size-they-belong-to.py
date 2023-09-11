class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        N = len(groupSizes)
        p = sorted(list(range(N)), key=lambda i:groupSizes[i])
        tmp = []
        res = []
        sz = 0
        for i in p:
            if sz == 0:
                sz = groupSizes[i]
            if sz > 0:
                tmp.append(i)
                sz -= 1
            if sz == 0:
                res.append(tmp[:])
                tmp = []
        return res