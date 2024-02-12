class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        res = []
        for n,k in queries:
            d = 1
            for i in range(2,int(sqrt(k))+2):
                cnt = 0
                while k%i == 0:
                    k //= i
                    cnt += 1
                d = d * comb(cnt+n-1, n-1) % 1000000007
            if k > 1:
                d = d * n % 1000000007
            res.append(d)
        return res