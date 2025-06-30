class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        cnt = Counter(nums)
        for a in cnt:
            if cnt[a+1]:
                res = max(res, cnt[a] + cnt[a+1])
        return res