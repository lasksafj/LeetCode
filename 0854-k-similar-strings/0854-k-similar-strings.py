class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbor(x):
            i = 0
            while x[i] == s2[i]:
                i += 1
            for j in range(i+1, len(x)):
                if x[j] == s2[i]:
                    yield x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
        
        q = deque([s1])
        vis = {s1}
        res = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == s2:
                    return res
                for nx in neighbor(x):
                    if nx not in vis:
                        vis.add(nx)
                        q.append(nx)
            res += 1
        return res