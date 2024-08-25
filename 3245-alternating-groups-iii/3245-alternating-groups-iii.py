from sortedcontainers import SortedSet
class BIT:
    def __init__(self, N):
        self.N = N
        self.T = [0]*(self.N+1)
        self.cur = 0

    def update(self, index, val):
        i = index+1
        while i <= self.N:
            self.T[i] += val
            i += i&(-i)
    
    def calc(self, index):
        res = 0
        i = index+1
        while i > 0:
            res += self.T[i]
            i -= i&(-i)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.calc(right) - self.calc(left-1)
    

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        N = len(colors)
        T1 = BIT(N+1)
        T2 = BIT(N+1)
        mp = {}
        def update(i,v):
            T1.update(i,v)
            T2.update(i,i*v)
            mp[i] = mp.get(i,0)+v
            if mp[i] == 0:
                del mp[i]
        
        A = SortedSet()
        for i in range(N):
            if colors[i] == colors[(i+1)%N]:
                # if A:
                #     update(i+1-A[-1], 1)
                A.add((i+1)%N)
        if A:
            for i in range(len(A)):
                # l = A[-1] - N
                # r = A[0]
                # update(r-l, 1)
                
                l = A[i]
                r = A[i+1] if i+1<len(A) else A[0]+N
                update(r-l, 1)
        else:
            update(N,2)
        
        def discard(A, idx):
            p = A.index(idx)
            l = A[p-1] if p>0 else A[-1] - N
            r = A[p+1] if p+1 < len(A) else A[0] + N
            # if len(A) > 1:
            #     update(idx-l, -1)
            #     update(r-idx, -1)
            #     update(r-l, 1)
            # else:
            #     update(N, 1)
            
            
            if len(A) == 1:
                update(r-idx, -1)
                update(N, 2)
            else:
                update(idx-l, -1)
                update(r-idx, -1)
                update(r-l, 1)
                
            A.discard(idx)
        
        def add(A, idx):
            if not A:
                update(N, -1)
                A.add(idx)
                return
            p = A.bisect_right(idx)
            l = A[p-1] if p>0 else A[-1]-N
            r = A[p] if p<len(A) else A[0]+N
            update(idx-l, 1)
            update(r-idx, 1)
            update(r-l, -1)
            A.add(idx)
            
        res = []
        # print(A, mp)
        for i in range(len(queries)):
            if queries[i][0] == 2:
                _,idx,c = queries[i]
                if colors[idx] == c:
                    continue
                colors[idx] = c
                p = A.bisect_left(idx)
                if idx in A:
                    discard(A, idx)
                else:
                    add(A, idx)
                # print(A, mp)
                if (idx+1)%N in A:
                    discard(A, (idx+1)%N)
                else:
                    add(A, (idx+1)%N)
                # print(A, mp)
            else:
                if not A:
                    res.append(N)
                    continue
                size = queries[i][1]
                a = T2.sumRange(size, N) + T1.sumRange(size, N) * (1-size)
                # print(T1.T)
                # print(T2.T)
                # print(size,'---',T2.sumRange(size, N) , T1.sumRange(size, N))
                res.append(a)
            
        return res