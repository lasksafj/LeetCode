class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        no_less_than_cur = 0
        cur = 0
        for n in nums:
            if n == target:
                no_less_than_cur += mp[cur]
                cur += 1
                mp[cur] += 1
            else:
                cur -= 1
                no_less_than_cur -= mp[cur]
                mp[cur] += 1
            res += no_less_than_cur
        return res