class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a,b = n//2,n-n//2
        c,d = m//2,m-m//2
        return a*d + b*c