class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        s,res = 0,0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            if s < 0:
                res = i+1
                s = 0
        return res