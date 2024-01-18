class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        m = defaultdict(list)
        for i,hat in enumerate(hats):
            for h in hat:
                m[h].append(i)
        # print(m)
        @cache
        def dfs(h,mask):
            # print(h,bin(mask))
            if h == 41:
                return mask == 0
            if h not in m:
                return dfs(h+1, mask)
            res = 0
            for p in m[h]:
                if (1<<p)&mask:
                    res = (res + dfs(h+1, mask^(1<<p))) % 1000000007
            return (res + dfs(h+1, mask)) % 1000000007
        return dfs(1, 2**len(hats)-1)