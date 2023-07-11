class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        m = {x:1 for x in range(1,maxValue+1)}
        res = maxValue
        for i in range(1,n):
            tmp = Counter()
            for k in m:
                for x in range(2, maxValue//k+1):
                    tmp[k*x] += m[k]
                    res += comb(n-1, i) * m[k]
            m = tmp
            res %= 10**9+7
        return res