class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [False] * n
        vis[0] = True
        q = deque([0])
        res = 1
        while q:
            cur = rooms[q.popleft()]
            for ne in cur:
                if not vis[ne]:
                    vis[ne] = True
                    q.append(ne)
                    res += 1
                    if res == n:
                        return True
        return res == n
                        