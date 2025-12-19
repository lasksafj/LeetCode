def f(edges, q):
    adj = defaultdict(list)
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    q = deque(set(q))
    res = set(q)
    while q:
        a = q.popleft()
        for ne in adj[a]:
            if ne not in res:
                res.add(ne)
                q.append(ne)
    return res


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        i = 0
        N = len(meetings)
        res = {0, firstPerson}
        while i < N:
            j = i
            start = []
            edges = []
            while j < N and meetings[j][2] == meetings[i][2]:
                a,b,_ = meetings[j]
                if a in res:
                    start.append(a)
                if b in res:
                    start.append(b)
                edges.append([a,b])
                j += 1
            res |= f(edges, start)
            i = j
        return list(res)