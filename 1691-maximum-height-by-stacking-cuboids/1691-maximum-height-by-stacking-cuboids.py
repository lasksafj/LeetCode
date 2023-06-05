class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        from itertools import permutations
        # cuboids = [sorted(cuboids[i]) for i in range(len(cuboids))]
        # cuboids.sort(key=lambda x: max(x[0]*x[1],x[0]*x[2],x[1]*x[2]) )
        # print(cuboids)
        vis = [False]*len(cuboids)
        @cache
        def dfs(pw, pl, ph):
            res = 0
            for i in range(len(cuboids)):
                if not vis[i]:
                    vis[i] = True
                    for w,l,h in list(permutations(cuboids[i])):
                        if pw <= w and pl <= l and ph <= h:
                            res = max(res, h + dfs(w, l, h))
                    vis[i] = False
            # res = max(res, dfs(pw, pl, ph))
            return res
        return dfs(0, 0, 0)
        
        # a = dfs(0, 0, 0, 0)
        # cuboids.sort(key=lambda x:min(x[0],x[1],x[2]))
        # # print(cuboids)
        # b = dfs(0, 0, 0, 0)
        # return max(a,b)