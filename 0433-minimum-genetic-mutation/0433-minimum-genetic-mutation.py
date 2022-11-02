class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        m = {}
        for s in bank:
            m[s] = inf
        if end not in m:
            return -1
        q = deque([start])
        res = 0
        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                cur = q.popleft()
                for i in range(8):
                    for c in ['A', 'C', 'G', 'T']:
                        if c == cur[i]:
                            continue
                        ncur = cur[0:i] + c + cur[i+1:]
                        # print(ncur, end)
                        if ncur == end:
                            return res
                        
                        if ncur in m and m[ncur] > res:
                            q.append(ncur)
                            m[ncur] = res
            
        return -1
                            