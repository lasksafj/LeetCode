class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        N = len(s)
        # only len(s) rotation, each rotation only 10 independent additions => len(s) * 10 state
        vis = set()
        q = deque([s])
        res = s
        while q:
            cur = q.popleft()
            res = min(res, cur)
            ncur = ''
            for i in range(N):
                ncur += str((int(cur[i]) + a)%10) if i%2 == 1 else cur[i]
            if ncur not in vis:
                vis.add(ncur)
                q.append(ncur)
            ncur = cur[N-b:] + cur[:N-b]
            if ncur not in vis:
                vis.add(ncur)
                q.append(ncur)
        return res