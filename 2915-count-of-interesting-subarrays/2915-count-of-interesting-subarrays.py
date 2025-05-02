class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        pre = 0
        res = 0
        for n in nums:
            pre = (pre + (n%modulo == k)) % modulo
            res += mp[(pre-k+modulo) % modulo]
            mp[pre] += 1
        return res