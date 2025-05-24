class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        T = {}
        for w in words:
            cur = T
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = cur.get('#', 0) + 1
        mp = defaultdict(deque)
        for c in T:
            mp[c] = deque([T[c]])
        res = 0
        for c in s:
            if c not in mp:
                continue
            for _ in range(len(mp[c])):
                ne = mp[c].popleft()
                if '#' in ne:
                    res += ne['#']
                for nc in ne:
                    if nc != '#':
                        mp[nc].append(ne[nc])

        return res
            