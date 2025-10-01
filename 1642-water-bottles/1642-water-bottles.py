class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 1 + (numExchange-1) -> numExchange water bottle
        # we can exchange maximum (numBottles-1)//(numExchange-1) times
        return numBottles + (numBottles-1)//(numExchange-1)