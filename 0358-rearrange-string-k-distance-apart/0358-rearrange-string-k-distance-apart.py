class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: return s
        cnt = Counter(s)
        n = len(s)
        pq = []
        for c,v in cnt.items():
            heappush(pq, [-v,c])
        res = ''
        while pq:
            A = []
            for _ in range(min(n,k)):
                if not pq: return ''
                v,c = heappop(pq)
                v = -v
                v -= 1
                if v:
                    A.append([v,c])
                res += c
                n -= 1
            for v,c in A:
                heappush(pq, [-v,c])
        return res