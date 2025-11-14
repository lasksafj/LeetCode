class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0]*(n+1) for _ in range(n+1)]
        for r1,c1,r2,c2 in queries:
            A[r1][c1] += 1
            A[r1][c2+1] -= 1
            A[r2+1][c1] -= 1
            A[r2+1][c2+1] += 1
        cur_diff = [0]*(n+1)
        res = []
        for row in A[:-1]:
            cur_diff = [c+r for c,r in zip(cur_diff,row)]
            res.append(list(accumulate(cur_diff))[:-1])
        return res