class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        def F(nums, d):
            s = sum(nums[:N//3])
            pq = []
            for n in nums[:N//3]:
                heappush(pq, n*d)
            res = [0]*N
            res[N//3-1] = s
            for i in range(N//3, N):
                if nums[i]*d > pq[0]:
                    c = heappop(pq)
                    c *= d
                    s = s-c+nums[i]
                    heappush(pq, nums[i]*d)
                res[i] = s
            return res
        L = F(nums, -1)
        R = F(nums[::-1], 1)[::-1]
        res = inf
        for i in range(N//3-1, 2*N//3):
            res = min(res, L[i] - R[i+1])
        return res