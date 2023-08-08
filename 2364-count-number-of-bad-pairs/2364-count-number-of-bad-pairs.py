class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i,n in enumerate(nums):
            m[n-i] += 1
        res = 0
        for n,cnt in m.items():
            res += (cnt-1)*cnt//2
        return len(nums)*(len(nums)-1)//2 - res