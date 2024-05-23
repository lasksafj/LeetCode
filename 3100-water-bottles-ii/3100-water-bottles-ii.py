class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles + empty >= numExchange:
            res += numBottles
            empty += numBottles
            empty -= numExchange
            numBottles = 1
            numExchange += 1
        return res + numBottles