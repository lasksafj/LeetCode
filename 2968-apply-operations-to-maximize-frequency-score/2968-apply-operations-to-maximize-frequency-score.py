class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        pre = [0]*(N+1)
        # print(nums)
        for i in range(N):
            pre[i+1] = pre[i] + nums[i]
        # print(pre)
        j = 0
        res = 0
        for i in range(N):
            mi = (i+j)//2
            while (mi-j)*nums[mi] - (pre[mi] - pre[j]) + (pre[i+1] - pre[mi+1]) - (i-mi)*nums[mi] > k:
                j += 1
                mi = (i+j)//2
            res = max(res, i-j+1)
        return res