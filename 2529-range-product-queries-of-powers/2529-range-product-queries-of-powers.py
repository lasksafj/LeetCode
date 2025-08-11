class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        A = []
        i = 0
        while n:
            if n&1:
                A.append(i)
            i += 1
            n >>= 1
        pre = list(accumulate(A, initial=0))
        return [(1<<(pre[b+1]-pre[a])) % MOD for a,b in queries]