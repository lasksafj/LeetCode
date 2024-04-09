class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        a = tickets[k]
        prev = defaultdict(int)
        for i in range(k):
            prev[tickets[i]] += 1
        
        N = len(tickets)
        cnt = Counter(tickets)
        res = 0
        d = 0
        # print(sorted(cnt.keys()))
        for kk,v in sorted(cnt.items()):
            # print(kk,v,N,kk-d)
            if kk == a:
                return res+N*(kk-d-1)+k+1
            res += N*(kk-d)
            if kk in prev:
                k -= prev[kk]
            N -= v
            d = kk
        return res