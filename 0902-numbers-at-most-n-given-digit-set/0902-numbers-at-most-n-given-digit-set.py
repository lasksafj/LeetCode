class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        A = sorted(digits)
        @cache
        def dfs(i, tight):
            if i == len(N):
                return 1
            res = 0
            for a in A:
                if tight and a > N[i]:
                    break
                res += dfs(i+1, tight&(a==N[i]))
            return res
        res = dfs(0,1)
        for i in range(1, len(N)):
            res += dfs(i,0)
        return res