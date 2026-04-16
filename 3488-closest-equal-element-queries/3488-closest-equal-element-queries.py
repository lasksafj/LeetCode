class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        mp = defaultdict(list)
        for i,n in enumerate(nums):
            mp[n].append(i)
        res = [-1]*N
        for n,A in mp.items():
            if len(A) == 1:
                continue
            for i,k in enumerate(A):
                if i:
                    res[k] = k-A[i-1]
                else:
                    res[k] = N-(A[i-1]-k)
                if i+1 < len(A):
                    res[k] = min(res[k], A[i+1]-k)
                else:
                    res[k] = min(res[k], N-(k-A[0]))
        return [res[q] for q in queries]