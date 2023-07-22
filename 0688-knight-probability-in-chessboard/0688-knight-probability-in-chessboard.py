class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        q = deque([(row,column,1)])
        while q and k > 0:
            nq = defaultdict(int)
            for _ in range(len(q)):
                x,y,v = q.popleft()
                for nx,ny in [[x+1,y+2],[x+1,y-2],[x-1,y+2],[x-1,y-2],[x+2,y-1],[x+2,y+1],[x-2,y+1],[x-2,y-1]]:
                    if 0 <= nx < n and 0 <= ny < n:
                        nq[(nx,ny)] += v*1/8
            for (x,y),v in nq.items():
                q.append((x,y,v))
            k -= 1
        return sum(q[i][2] for i in range(len(q)))