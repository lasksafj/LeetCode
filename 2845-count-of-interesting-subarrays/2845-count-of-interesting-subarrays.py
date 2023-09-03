class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = 0
        mp = defaultdict(int)
        mp[0] = 1
        pre = 0
        for n in nums:
            pre += (n%modulo == k)
            if pre >= modulo:
                pre -= modulo
            res += mp[(pre-k+modulo)%modulo]
            mp[pre] += 1
        return res