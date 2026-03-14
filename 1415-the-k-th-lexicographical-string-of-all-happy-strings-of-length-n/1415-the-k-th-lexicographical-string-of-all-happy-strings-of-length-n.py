class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        kk = 3 * pow(2, n-1)
        k -= 1
        if k >= kk: return ''
        A = ['a','b','c']
        res = [A[k//(kk//3)]]
        k %= kk//3
        kk //= 3
        for i in range(n-1):
            A.remove(res[-1])
            res.append(A[k//(kk//2)])
            k %= kk//2
            kk //= 2
            A = ['a','b','c']
        return ''.join(res)