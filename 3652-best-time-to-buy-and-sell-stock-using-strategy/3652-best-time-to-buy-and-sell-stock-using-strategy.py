class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        pref = list(accumulate(prices, initial=0))
        pref2 = [0]*(len(prices)+1)
        for i in range(1, len(prices)+1):
            pref2[i] = pref2[i-1] + prices[i-1]*strategy[i-1]
        res = pref2[-1] - pref2[0]
        for i in range(k, len(prices)+1):
            d = pref2[-1] - pref2[i] + pref[i] - pref[i-k//2] + pref2[i-k] - pref2[0]
            res = max(res, d)
        return res