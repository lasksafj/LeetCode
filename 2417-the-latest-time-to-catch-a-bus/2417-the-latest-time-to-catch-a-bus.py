class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pq = []
        A = []
        i = 0
        for b in buses:
            while i < len(passengers) and passengers[i] <= b:
                heappush(pq, passengers[i])
                i += 1
            k = 0
            while k < capacity and pq:
                A.append(heappop(pq))
                k += 1
        if not pq and k < capacity:
            res = buses[-1]
        else:
            res = A[-1]
        while A and A[-1] == res:
            A.pop()
            res -= 1
        return res
        