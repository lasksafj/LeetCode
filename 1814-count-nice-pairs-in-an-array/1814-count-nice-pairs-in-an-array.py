class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        mp = defaultdict(int)
        for n in nums:
            mp[n-rev(n)] += 1
        res = 0
        for _,k in mp.items():
            res = (res + (k*(k-1))//2) % 1000000007
        return res