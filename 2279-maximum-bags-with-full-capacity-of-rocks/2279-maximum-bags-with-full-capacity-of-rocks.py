class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        idx = sorted(list(range(n)), key=lambda x: capacity[x]-rocks[x])
        capacity = [capacity[i] for i in idx]
        rocks = [rocks[i] for i in idx]
        i = 0
        while i < n and additionalRocks > 0:
            additionalRocks -= (capacity[i] - rocks[i])
            i += 1
        return i if additionalRocks >= 0 else i-1