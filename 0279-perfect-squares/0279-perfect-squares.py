class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: 
            return 1
        for i in range(1, int(sqrt(n)+1)):
            if int(sqrt(n-i*i))**2 == n - i*i:
                return 2
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        return 3