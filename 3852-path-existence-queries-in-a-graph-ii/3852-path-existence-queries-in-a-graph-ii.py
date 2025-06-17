class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        A = sorted([[num,i] for i,num in enumerate(nums)])
        newpos = [0]*n
        for k,(num,i) in enumerate(A):
            newpos[i] = k
        nums.sort()
        i = 0
        f = [-1]*n
        while i < n:
            j = i+1
            while j < n and nums[j] <= nums[j-1] + maxDiff:
                j += 1
            nk = i
            for k in range(i,j):
                while nk < n and nums[k] + maxDiff >= nums[nk]:
                    nk += 1
                if k < nk-1:
                    f[k] = nk-1
            i = j
        p = [[-1]*20 for _ in range(n+1)]
        for i in range(n):
            p[i][0] = f[i]
        for j in range(1, 20):
            for i in range(n):
                p[i][j] = p[p[i][j-1]][j-1]
        res = []
        for a,b in queries:
            a,b = newpos[a], newpos[b]
            if a == b:
                res.append(0)
                continue
            if a > b:
                a,b = b,a
            d = 0
            for k in range(19,-1,-1):
                if a < p[a][k] < b:
                    d |= 1<<k
                    a = p[a][k]
            a = p[a][0]
            d += 1
            res.append(d if a >= b else -1)
        return res