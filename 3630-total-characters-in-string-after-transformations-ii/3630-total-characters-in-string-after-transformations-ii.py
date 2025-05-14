def mat_mul(A, B, mod):
    res = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B[0])):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= mod
    return res
def mat_pow(A, n, mod):
    res = [[int(i==j) for j in range(len(A))] for i in range(len(A))]
    while n:
        if n&1:
            res = mat_mul(res, A, mod)
        A = mat_mul(A, A, mod)
        n >>= 1
    return res


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9+7
        A = [[0]*26]
        for c in s:
            A[0][ord(c)-97] += 1
        B = [[0]*26 for _ in range(26)]
        for i in range(len(nums)):
            for j in range(i+1, i+1+nums[i]):
                B[i][j%26] = 1
        A = mat_mul(A, mat_pow(B, t, mod), mod)
        return sum(A[0]) % mod