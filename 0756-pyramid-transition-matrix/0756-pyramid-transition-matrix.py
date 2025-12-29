class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a,b,c in allowed:
            mp[a,b].append(c)
        N = len(bottom)
        def dfs(last, cur):
            if len(last) == 1:
                return True
            if len(cur) == len(last)-1:
                return dfs(cur, '')
            j = len(cur)
            for c in mp[last[j], last[j+1]]:
                cur += c
                if dfs(last, cur):
                    return True
                cur = cur[:-1]
            return False
        return dfs(bottom, '')