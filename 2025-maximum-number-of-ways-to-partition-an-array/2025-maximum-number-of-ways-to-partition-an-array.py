class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        R = defaultdict(int)
        L = defaultdict(int)
        a,b = 0,0
        N = len(nums)
        for i in range(N-1,-1,-1):
            b += nums[i]
            R[b] += 1
        s = b
        res = 0
        if s%2 == 0:
            res = R[s//2] - (s==s//2)
        for i in range(N):
            R[b] -= 1
            new_s = s+k-nums[i]
            if (new_s) % 2 == 0:
                res = max(res, R[new_s//2] + L[new_s//2])
            b -= nums[i]
            a += nums[i]
            L[a] += 1

        return res