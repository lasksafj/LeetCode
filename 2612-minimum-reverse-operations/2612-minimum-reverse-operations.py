class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban_set = set(banned)
        from sortedcontainers import SortedList
        good = [SortedList() for _ in range(2)]
        res = [-1]*n
        for i in range(n):
            if i not in ban_set and i != p:
                good[i&1].add(i)
        q = deque([p])
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                res[cur] = step
                l = abs(cur-(k-1))
                r = n-1-(abs(n-1-(cur+k-1)))
                a = bisect_left(good[l&1], l)
                while a < len(good[l&1]) and good[l&1][a] <= r:
                    q.append(good[l&1][a])
                    good[l&1].pop(a)
            step += 1
        return res