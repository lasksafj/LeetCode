class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        no1 = sum(nums)
        if no1 <= 1:
            return 0
        j = 0
        res = inf
        cur = 0
        cur_len = 0
        for i in range(N*2):
            i = i%N
            cur += nums[i]
            cur_len += 1
            if cur_len == no1:
                res = min(res, no1-cur)
                cur -= nums[j]
                j = (j+1)%N
                cur_len -= 1
        return res