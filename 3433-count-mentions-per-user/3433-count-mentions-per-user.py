class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        on = set(range(numberOfUsers))
        off = deque()
        res = [0]*numberOfUsers
        for typ, t, s in sorted(events, key=lambda x: [int(x[1]), x[0][0] == 'M']):
            t = int(t)
            while off and off[0][1] <= t:
                on.add(off.popleft()[0])
            if typ == 'MESSAGE':
                if s == 'HERE':
                    for u in on:
                        res[u] += 1
                elif s == 'ALL':
                    for u in range(numberOfUsers):
                        res[u] += 1
                else:
                    for u in s.split():
                        res[int(u[2:])] += 1
            else:
                u = int(s)
                on.discard(u)
                off.append([u, t+60])
        return res