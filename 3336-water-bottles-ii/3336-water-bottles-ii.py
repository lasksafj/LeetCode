class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # t: number of exchanges
        # no exchanged empty = sum(numExchange + i) for i=0->t-1
        # total bottles: numBottles + t
        # no exchanged empty <= total
        # t*numExchange + t(t-1)/2 <= numBottles + t
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        delta = b * b - 4 * a * c
        t = math.ceil((-b + math.sqrt(delta)) / (2 * a))
        return numBottles + t - 1