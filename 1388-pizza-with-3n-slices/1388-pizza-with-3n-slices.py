class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @cache
        def dfs(i,k,end):
            if i >= end:
                return 0 if k == len(slices)//3 else -inf
            return max(dfs(i+2,k+1,end) + slices[i], dfs(i+1,k,end))
        return max(dfs(0,0,len(slices)-1), dfs(1,0,len(slices)))