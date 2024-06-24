class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        A = [0]*(N+k)
        res = 0
        s = 0
        for i in range(N-k+1):
            s += A[i]
            # print(i,s)
            cur = (s+nums[i])%2
            if cur == 0:
                A[i] += 1
                A[i+k] -= 1
                s += 1
                res += 1
        for i in range(N-k+1,N):
            s += A[i]
            cur = (s+nums[i])%2
            if cur == 0:
                return -1
        return res