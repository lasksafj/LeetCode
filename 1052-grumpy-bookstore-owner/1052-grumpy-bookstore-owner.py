class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        # max unsatisfied in minutes
        ma_unsatisfied = 0
        unsatisfied = 0
        for i in range(N):
            if i < minutes:
                unsatisfied += customers[i]*grumpy[i]
                ma_unsatisfied = unsatisfied
            else:
                unsatisfied += customers[i]*grumpy[i] - customers[i-minutes]*grumpy[i-minutes]
                ma_unsatisfied = max(ma_unsatisfied, unsatisfied)
        res = ma_unsatisfied
        for c,g in zip(customers, grumpy):
            res += c*(1-g)
        return res