class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        m = defaultdict(int)
        for a,b in trust:
            m[b] += 1
            m[a] -= 1
        for i in range(1,n+1):
            if m[i] == n-1:
                return i
        return -1