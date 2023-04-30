class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        f1,f2 = list(range(n+1)),list(range(n+1))
        r1,r2 = [0]*(n+1),[0]*(n+1)
        def root(a,f):
            if a == f[a]:
                return a
            return root(f[a], f)
        def union(a,b,f,r):
            a,b = root(a,f),root(b,f)
            if a == b:
                return
            if r[a] < r[b]:
                f[a] = b
            elif r[a] > r[b]:
                f[b] = a
            else:
                f[b] = a
                r[a] += 1
        def check(a,b,f):
            a,b = root(a,f),root(b,f)
            if a == b:
                return True
            return False
        res = 0
        for t,a,b in edges:
            if t == 3:
                if check(a,b,f1) and check(a,b,f2):
                    res += 1
                else:
                    union(a,b,f1,r1)
                    union(a,b,f2,r2)
        for t,a,b in edges:
            if t == 2:
                if check(a,b,f2):
                    res += 1
                else:
                    union(a,b,f2,r2)
            elif t == 1:
                if check(a,b,f1):
                    res += 1
                else:
                    union(a,b,f1,r1)
        for i in range(1,n+1):
            if not check(1,i,f1) or not check(1,i,f2):
                return -1
        return res
            