class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        wl,wr = [],[]
        nwl,nwr = [],[]
        for i in range(len(time)):
            a,b,c,d = time[i]
            heapq.heappush(nwl, [-(a+c), -i])
        cur = 0
        
        while 1:
            # print(wl,'->',nwl,'---',nwr,'<-',wr)
            # print(cur, n)
            # print('--------------')
            if not nwl and not nwr:
                a = wl[0][0] if wl else inf
                b = wr[0][0] if wr else inf
                cur = min(a,b)
            
            # print(wl,'->',nwl,'---',nwr,'<-',wr)
            # print(cur, n)
            # print('--------------')

            while wl and wl[0][0] <= cur:
                a,b,c = heapq.heappop(wl)
                heapq.heappush(nwl, [b,c])
                
            while wr and wr[0][0] <= cur:
                a,b,c = heapq.heappop(wr)
                heapq.heappush(nwr, [b,c])

            if nwr:
                _,w = heapq.heappop(nwr)
                w = -w
                cur += time[w][2]
                if n == 0 and not wr and not nwr:
                    return cur
                heapq.heappush(wl, [cur+time[w][3], -(time[w][0]+time[w][2]), -w])
            else:
                if nwl and n > 0:
                    n -= 1
                    _, w = heapq.heappop(nwl)
                    w = -w
                    cur += time[w][0]
                    heapq.heappush(wr, [cur+time[w][1], -(time[w][0]+time[w][2]), -w])
                else:
                    cur = wr[0][0]
            
        return 0
                
        