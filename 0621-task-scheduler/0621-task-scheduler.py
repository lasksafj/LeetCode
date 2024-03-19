class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        for task,cnt in Counter(tasks).items():
            heappush(pq, (-cnt, task))
        res = 0
        q = deque([(0,'')]*(n+1))
        N = len(tasks)
        while N > 0:
            cnt, task = q.popleft()
            if task and cnt:
                heappush(pq, (-cnt, task))
            # print(pq, N)
            if pq:
                N -= 1
                cnt,task = heappop(pq)
                cnt = -cnt
                cnt -= 1
                q.append((cnt, task))
            else:
                q.append((0, ''))
            res += 1
        return res