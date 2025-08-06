class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        A = sorted(list(range(N)), key=lambda x: [sum(int(d) for d in str(nums[x])), nums[x]] )
        mp = {}
        for i,a in enumerate(A):
            mp[a] = i
        res = 0
        vis = set()
        for i in range(N):
            step = 0
            while i not in vis:
                vis.add(i)
                i = mp[i]
                step += 1
            res += max(0, step-1)
        return res