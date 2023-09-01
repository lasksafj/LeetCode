class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heappush(pq, [-a, 'a'])
        if b > 0:
            heappush(pq, [-b, 'b'])
        if c > 0:
            heappush(pq, [-c, 'c'])
        s = '--'
        i = 1
        prev_n,prev_ch = 0, '-'
        while pq:
            n, ch = heappop(pq)
            n = -n
            if s[i] == ch and s[i] == s[i-1]:
                prev_n,prev_ch = n,ch
            else:
                s += ch
                i += 1
                n -= 1
                if n > 0:
                    heappush(pq, [-n, ch])
                if prev_n > 0:
                    heappush(pq, [-prev_n, prev_ch])
                    prev_n = 0
        return s[2:]