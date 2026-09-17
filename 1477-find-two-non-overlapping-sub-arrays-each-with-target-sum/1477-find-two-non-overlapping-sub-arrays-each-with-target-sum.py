class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        res = [inf]*N
        j = 0
        cur = 0
        ans = inf
        for i in range(N):
            cur += arr[i]
            while cur > target:
                cur -= arr[j]
                j += 1        
            if cur == target:
                ans = min(ans, i-j+1 + res[j-1])
                res[i] = min(res[i-1], i-j+1)
            else:
                res[i] = res[i-1]
        return ans if ans < inf else -1