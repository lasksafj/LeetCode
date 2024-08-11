class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        N = len(nums)
        A = []
        mp = defaultdict(int)
        for i in range(N//2):
            a,b = nums[i],nums[N-i-1]
            mp[abs(a-b)] += 1
            A.append(max(a,b,k-a,k-b))
        A.sort()
        B = []
        for k,v in mp.items():
            B.append([v,k])
        B.sort(reverse=True)
        # print(A)
        # print(B)
        res = inf
        for no_pairs,dist in B:
            p = bisect_left(A,dist)
            cur = N//2-p + p*2 - no_pairs
            res = min(res, cur)
        return res