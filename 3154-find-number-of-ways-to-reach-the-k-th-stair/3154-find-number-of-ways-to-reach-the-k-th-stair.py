class Solution:
    def waysToReachStair(self, k: int) -> int:
        res = 0
        for n in range(50):
            for i in range(n+2):
                if 1 + ((1<<n) - 1) - i == k:
                    res += comb(n+1,i)
                    # print(n,i,comb(n+1,i))
        return res