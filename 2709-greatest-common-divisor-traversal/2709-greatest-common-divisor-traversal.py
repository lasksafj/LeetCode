class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        f = list(range(n))
        r = [0]*n
        def root(x):
            if x == f[x]:
                return x
            return root(f[x])
        def union(a,b):
            a,b = root(a),root(b)
            if a == b:
                return
            if r[a] < r[b]:
                f[a] = b
            elif r[a] > r[b]:
                f[b] = a
            else:
                f[a] = b
                r[b] += 1
        
        m = {}
        for i,x in enumerate(nums):
            for p in range(2, int(sqrt(x))+1):
                if x%p == 0:
                    if p in m:
                        union(i, m[p])
                    else:
                        m[p] = i
                    while x%p == 0:
                        x //= p
            if x > 1:
                if x in m:
                    union(i, m[x])
                else:
                    m[x] = i
        return all(root(i) == root(0) for i in range(n))