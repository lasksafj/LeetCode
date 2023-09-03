class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        A = []
        for n in nums:
            if n%modulo == k:
                A.append(1)
            else:
                A.append(0)
        res = 0
        mp = defaultdict(int)
        mp[0] = 1
        pre = 0
        for n in A:
            pre += n
            if pre >= modulo:
                pre -= modulo
            res += mp[(pre-k+modulo)%modulo]
            mp[pre] += 1
        return res