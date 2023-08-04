class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        @cache
        def dfs(i):
            # print(i)
            res = 0
            for j in range(i+1, min(N,i+d+1)):
                if arr[j] < arr[i]:
                    res = max(res, dfs(j))
                else:
                    break
            for j in range(i-1, max(-1,i-d-1,-1), -1):
                if arr[j] < arr[i]:
                    res = max(res, dfs(j))
                else:
                    break
            return res + 1
        res = 0
        # print(dfs(10))
        for i in range(N):
            res = max(res, dfs(i))
        return res
                    