class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]
        for i in range(3, n+1):
            f[i%3] = f[(i-1)%3] + f[(i-2)%3] + f[(i-3)%3]
        return f[n%3]