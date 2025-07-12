class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dfs(l,r,n):
            if l == r:
                return 1,1
            if l > r:
                l,r = r,l
            nn = (n+1)//2
            res = [inf,-inf]
            for nl in range(1, l+1):
                nr = l-nl+1
                while nl+nr <= min(r,nn):
                    if l-nl+r-nr <= n//2:
                        mi,ma = dfs(nl,nr,nn)
                        res[0] = min(res[0], mi+1)
                        res[1] = max(res[1], ma+1)
                    nr += 1
            return res

        l = firstPlayer
        r = n-secondPlayer+1
        return dfs(l,r,n)