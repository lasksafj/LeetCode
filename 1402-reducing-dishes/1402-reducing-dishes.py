class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dfs(i, k):
            # print(i,k)
            if i == len(satisfaction):
                return 0
            # res = -99999
            # for ne in range(i+1, len(satisfaction)+1):
            #     res = max(res, satisfaction[i]*k + dfs(ne, k+1))
                
            return max(satisfaction[i]*k + dfs(i+1,k+1), dfs(i+1,k))
            # return res
        return dfs(0,1)
        