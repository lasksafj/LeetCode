class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(s)
        pq = [[-cnt,ch] for ch,cnt in mp.items()]
        heapify(pq)
        prev_cnt,prev_ch = -1,''
        res = ''
        while pq:
            cnt,ch = heappop(pq)
            res += ch
            if prev_cnt > 0:
                heappush(pq, [-prev_cnt,prev_ch])
            prev_cnt,prev_ch = -cnt - 1, ch
        return res if prev_cnt == 0 else ''