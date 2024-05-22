from sortedcontainers import SortedList
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        cnt = Counter(s)
        k = cnt['?']
        pq = [[cnt[ch],ch] for ch in ascii_lowercase]
        heapify(pq)
        A = []
        for _ in range(k):
            d,ch = heappop(pq)
            A.append(ch)
            d += 1
            heappush(pq, [d,ch])
        A.sort()
        res = []
        i = 0
        for ch in s:
            if ch == '?':
                res.append(A[i])
                i += 1
            else:
                res.append(ch)
        return ''.join(res)