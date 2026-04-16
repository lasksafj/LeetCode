class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        mp = defaultdict(lambda: SortedList())
        for i,n in enumerate(nums):
            mp[n].add(i)
        res = []
        for i in queries:
            n = nums[i]
            A = mp[n]
            if len(A) == 1:
                res.append(-1)
                continue
            A.remove(i)
            j = A.bisect_right(i)
            if j:
                a = i - A[j-1]
            else:
                a = N - (A[-1]-i)
            if j < len(A):
                b = A[j] - i
            else:
                b = N - (i-A[0])
            res.append(min(a,b))
            A.add(i)
        return res