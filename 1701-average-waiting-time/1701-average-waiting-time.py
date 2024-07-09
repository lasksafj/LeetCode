class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        res = 0
        for a,b in customers:
            t = max(t,a)
            t += b
            res += t-a
        return res/len(customers)