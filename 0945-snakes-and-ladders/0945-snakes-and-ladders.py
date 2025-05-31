class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        mp = {}
        d = 1
        for i,row in enumerate(board[::-1]):
            if i&1: row = row[::-1]
            for ne in row:
                mp[d] = ne if ne > -1 else d
                d = d+1
        q = deque([1])
        vis = set()
        res = 0
        while q:
            for _ in range(len(q)):
                d = q.popleft()
                if d == N**2:
                    return res
                for ne in range(d+1, min(N**2, d+6) + 1):
                    ne = mp[ne]
                    if ne not in vis:
                        vis.add(ne)
                        q.append(ne)
            res += 1
        return -1