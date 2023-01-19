class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = defaultdict(int)
        a = nums[0]
        m[a%k] += 1
        for i in range(1,n):
            a += nums[i]
            m[a%k] += 1
        res = 0
        for a,b in m.items():
            if a == 0:
                res += b
            res += (b-1)*b//2
        return res
        