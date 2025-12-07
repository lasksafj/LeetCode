class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (low&1) ^ (high&1) == 0:
            return (high-low)//2 + (low&1)
        return (high+1-low)//2