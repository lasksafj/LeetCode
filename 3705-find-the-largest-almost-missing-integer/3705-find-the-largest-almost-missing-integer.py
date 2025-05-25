class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        cnt = Counter(nums)
        if k == 1:
            return max([x for x in cnt if cnt[x] == 1] + [-1])
        a,b = nums[0],nums[-1]
        return max(-1, a if cnt[a] == 1 else -inf, b if cnt[b] == 1 else -inf)