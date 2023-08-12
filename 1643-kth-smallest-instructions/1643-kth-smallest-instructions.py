class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        @cache
        def dfs(h,v,k):
            if h == 0 and v == 0:
                return ''
            elif h == 0:
                return 'V' + dfs(h,v-1,k)
            elif v == 0:
                return 'H' + dfs(h-1,v,k)
            c = comb(h+v-1, v)
            if k <= c:
                return 'H' + dfs(h-1,v,k)
            return 'V' + dfs(h,v-1,k-c)
        return dfs(destination[1], destination[0],k)