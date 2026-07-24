class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        res = set()
        P = {0}
        for i in range(N):
            for p in P:
                res.add(p^nums[i])
            for j in range(N):
                P.add(nums[i]^nums[j])
            if len(res) == 2048:
                return 2048
        return len(res)