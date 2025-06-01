class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        A = nums + nums
        mp = defaultdict(lambda:-inf)
        L = [inf]*N
        for i,a in enumerate(A):
            L[i%N] = min(L[i%N], i - mp[a])
            mp[a] = i
        mp = defaultdict(lambda: inf)
        for i in range(len(A)-1,-1,-1):
            L[i%N] = min(L[i%N], mp[A[i]] - i)
            mp[A[i]] = i
        res = []
        for q in queries:
            d = L[q]
            res.append(d if d < N else -1)
        return res