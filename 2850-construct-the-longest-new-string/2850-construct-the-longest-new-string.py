class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @cache
        def dfs(x,y,z,prev):
            a = b = 0
            if prev == 1 and y:
                a = dfs(x,y-1,z, 2) + 2
            if prev == 2 or prev == 3:
                b = max(dfs(x-1,y,z,1) if x else -2, dfs(x,y,z-1,3) if z else -2) + 2
            return max(a,b)
        return max(dfs(x-1,y,z,1), dfs(x,y-1,z,2), dfs(x,y,z-1,3)) + 2