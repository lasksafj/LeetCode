class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i,n in enumerate(tickets):
            if i <= k:
                res += min(tickets[k], tickets[i])
            else:
                res += min(tickets[k]-1, tickets[i])
        return res