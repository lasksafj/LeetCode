class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        def F(arr):
            res = [inf]*N
            j = 0
            cur = 0
            for i in range(N):
                cur += arr[i]
                while cur > target:
                    cur -= arr[j]
                    j += 1
                if cur == target:
                    res[i] = min(res[i-1], i-j+1)
                else:
                    res[i] = res[i-1]
            return res
        res = inf
        L = F(arr)
        R = F(arr[::-1])[::-1]
        for i in range(N-1):
            res = min(res, L[i]+R[i+1])
                
        return res if res < inf else -1