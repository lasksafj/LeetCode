class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Note that we won't have more than 31 values in the hash map. This is because the number of bits in values is decreasing.
        mp = defaultdict(int)
        res = 0
        for n in nums:
            n_mp = defaultdict(int)
            for v,cnt in list(mp.items()):
                n_mp[v&n] += cnt
            n_mp[n] += 1
            res += n_mp[k]
            mp = n_mp
        return res