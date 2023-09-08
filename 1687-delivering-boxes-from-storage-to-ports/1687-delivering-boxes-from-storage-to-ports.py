class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        @lru_cache(None)
        def backtrack(i):
            if i > n-1: return 0

            j = k = i
            b = w = extra = 0
            while j < n and b < maxBoxes and w + boxes[j][1] <= maxWeight:
                b += 1
                w += boxes[j][1]
                if j != i and boxes[j][0] != boxes[j-1][0]:
                    extra += 1
                    k = j
                j += 1

            trip = 2 + extra + backtrack(j)
            if k != i:
                trip = min(trip, 1 + extra + backtrack(k))
            return trip

        return backtrack(0)