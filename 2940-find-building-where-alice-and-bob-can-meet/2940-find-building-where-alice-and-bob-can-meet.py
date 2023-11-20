class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = max(heights)+1

        t = defaultdict(lambda:inf)

        def modify(p, value, t):
            p += n
            t[p] = value
            while p > 1:
                t[p>>1] = min(t[p] , t[p^1])
                p >>= 1


        def query( l,  r, t):
            res = inf
            l += n
            r += n
            while l < r:
                if l&1:
                    res = min(res , t[l])
                    l += 1
                if r&1:
                    r -= 1
                    res = min(res , t[r])
                l >>= 1
                r >>= 1
            return res
        
        A = []
        res = [-1]*len(queries)
        for i,(x,y) in enumerate(queries):
            a,b = min(x,y),max(x,y)
            if a != b and heights[a] >= heights[b]:
                A.append([max(a,b), max(heights[a],heights[b]), i])
            else:
                res[i] = b
        A.sort()
        j = len(A)-1
        if A == []:
            return res
        # print(A)

        for i in range(len(heights)-1,-1,-1):
            h = heights[i]
            
            while j >= 0 and i == A[j][0]:
                p = query(A[j][1]+1, n, t)
                res[A[j][2]] = p
                j -= 1
            modify(h,i,t)
            
        # print(res)
        return [v if v < inf else -1 for v in res]
            