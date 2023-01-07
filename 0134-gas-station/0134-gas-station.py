class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total,s,res = 0,0,0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if s < 0:
                res = i+1
                s = 0
        return res if total >= 0 else -1