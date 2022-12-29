class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        pq = []
        res = []
        cur = 0
        i = 0
        idx = 0
        tasks = sorted([[t[0],t[1],i] for i,t in enumerate(tasks)])
        while i < n or pq:
            if not pq and i < n and cur < tasks[i][0]:
                cur = tasks[i][0]
            while i < n and tasks[i][0] <= cur:
                a,b,idx = tasks[i]
                heapq.heappush(pq, [b,idx])
                i += 1
            if pq:
                b,ii = heapq.heappop(pq)
                cur += b
                res.append(ii)
            
        return res
                

        
        