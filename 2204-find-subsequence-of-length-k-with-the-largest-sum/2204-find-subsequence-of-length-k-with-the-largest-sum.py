class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(sorted(nums)[-k:])
        res = []
        for n in nums:
            if mp[n]:
                res.append(n)
                mp[n] -= 1
        return res