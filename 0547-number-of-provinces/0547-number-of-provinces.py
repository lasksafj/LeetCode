class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def dfs(i):
            vis.add(i)
            for ne in range(n):
                if ne != i and ne not in vis and isConnected[i][ne]:
                    dfs(ne)
        vis = set()
        res = 0
        for i in range(n):
            if i not in vis:
                res += 1
                dfs(i)
        return res