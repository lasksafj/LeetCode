class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        bricks_use = 0
        for i in range(len(heights)-1):
            if heights[i+1] > heights[i]:
                bricks_use += heights[i+1] - heights[i]
                heappush(pq, -(heights[i+1] - heights[i]))
                if bricks_use > bricks:
                    a = -heappop(pq)
                    bricks_use -= a
                    ladders -= 1
                    if ladders < 0:
                        return i
        return len(heights)-1