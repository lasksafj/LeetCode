class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = []
        cnt = Counter(s)
        for c in cnt:
            heappush(pq, (-ord(c), cnt[c]))
        res = []
        while pq:
            ch,v = heappop(pq)
            if v <= repeatLimit:
                res += [ch]*v
            else:
                res += [ch]*(repeatLimit)
                v -= repeatLimit
                if not pq:
                    break
                ch2,v2 = heappop(pq)
                res += [ch2]
                v2 -= 1
                heappush(pq, (ch,v))
                if v2 > 0:
                    heappush(pq, (ch2,v2))
        return ''.join(chr(-ch) for ch in res)