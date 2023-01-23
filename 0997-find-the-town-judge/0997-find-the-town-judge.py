class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ind = defaultdict(int)
        outd = defaultdict(int)
        for a,b in trust:
            ind[b] += 1
            outd[a] += 1
        for i in range(1,n+1):
            if ind[i] == n-1 and outd[i] == 0:
                return i
        return -1