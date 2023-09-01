class Solution:
    def countBits(self, n: int) -> List[int]:
        l,r,res = 0,0,[0]*(n+1)
        for i in range(1,n+1):
            if l < r:
                res[i] = res[l] + res[r]
                l += 1
            else:
                l = 1
                r = i
                res[i] = 1
        return res