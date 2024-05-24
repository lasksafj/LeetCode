class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        if N%2:
            res = 0
            mi = nums[N//2]
            if k < mi:
                for i in range(N//2,-1,-1):
                    if nums[i] > k:
                        res += nums[i] - k
                    else:
                        return res
            elif k > mi:
                for i in range(N//2, N):
                    if nums[i] < k:
                        res += k - nums[i]
                    else:
                        return res
            return res
        else:
            mi1,mi2 = nums[N//2-1],nums[N//2]
            if mi1 <= k <= mi2:
                return mi2-k
            res = 0
            if k < mi1:
                for i in range(N//2,-1,-1):
                    if nums[i] > k:
                        res += nums[i] - k
                    else:
                        return res
            else:
                for i in range(N//2, N):
                    if nums[i] < k:
                        res += k - nums[i]
                    else:
                        return res
            return res