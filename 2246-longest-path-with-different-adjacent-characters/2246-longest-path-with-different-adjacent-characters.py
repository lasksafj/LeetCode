class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        child = defaultdict(list)
        n = len(parent)
        for i in range(1, n):
            child[parent[i]].append(i)

        res = [0]
        def dfs(cur):
            a,b = 0,0
            for ch in child[cur]:
                c = dfs(ch)
                if s[ch] != s[cur]:
                    if c > a:
                        b = a
                        a = c
                    elif c > b:
                        b = c
            
            res[0] = max(res[0], a+b+1)
            return a+1
        dfs(0)
        return res[0]
            