class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(n):
            A = [0]*(n+1)
            for a,b,c,d in queries:
                if a <= i <= c:
                    A[b] += 1
                    A[d+1] -= 1
            res.append(list(accumulate(A))[:-1])
        return res