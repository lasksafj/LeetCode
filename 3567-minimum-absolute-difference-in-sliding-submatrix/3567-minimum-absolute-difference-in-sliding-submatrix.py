class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        res = [[0]*(N-k+1) for _ in range(M-k+1)]
        def add(A, B, freq, d):
            if d not in freq:
                freq[d] = 1
                i = A.bisect_right(d)
                if 0 < i < len(A):
                    B.remove(A[i]-A[i-1])
                if i:
                    B.add(d-A[i-1])
                if i < len(A):
                    B.add(A[i]-d)
                A.add(d)
            else:
                freq[d] += 1
        def remove(A, B, freq, d):
            freq[d] -= 1
            if freq[d] == 0:
                i = A.bisect_left(d)
                if 0 < i < len(A)-1:
                    B.add(A[i+1]-A[i-1])
                if i:
                    B.remove(d-A[i-1])
                if i+1 < len(A):
                    B.remove(A[i+1]-d)
                del freq[d]
                A.remove(d)
            
        for i in range(M-k+1):
            A = SortedList()
            B = SortedList()
            freq = {}
            for r in range(i,i+k):
                for c in range(k):
                    add(A,B,freq,grid[r][c])
            res[i][0] = B[0] if B else 0
            for j in range(N-k):
                for r in range(i,i+k):
                    remove(A,B,freq,grid[r][j])
                    add(A,B,freq,grid[r][j+k])
                res[i][j+1] = B[0] if B else 0
        return res