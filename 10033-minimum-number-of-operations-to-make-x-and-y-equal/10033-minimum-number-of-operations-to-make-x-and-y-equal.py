class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y-x
        ma = x + max(5-x%5, 11-x%11)
        vis = [0]*(ma+1)
        q = deque([x])
        res = 0
        while q:
            # print(q)
            for _ in range(len(q)):
                a = q.popleft()
                if a == y:
                    return res
                tmp = [a-1,a+1]
                if a%11==0:
                    tmp.append(a//11)
                if a%5==0:
                    tmp.append(a//5)
                for n in tmp:
                    if n <= ma and not vis[n]:
                        vis[n] = 1
                        q.append(n)
            res += 1
        return res