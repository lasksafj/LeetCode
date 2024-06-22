class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        mp = defaultdict(int)
        mp[0] = 1
        for n in nums:
            cur += n%2
            res += mp[cur-k]
            mp[cur] += 1
        return res