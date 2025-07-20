class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        T = {}
        for path in paths:
            cur = T
            for c in path:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
        mp = defaultdict(int)
        def dfs(cur):
            if not cur:
                cur['#'] = ''
                return
            res = []
            for c,node in cur.items():
                dfs(node)
                s = c + '(' + node['#'] + ')'
                res.append(s)
            res.sort()
            cur['#'] = ''.join(res)
            mp[cur['#']] += 1
        dfs(T)

        res = []
        def dfs2(cur, path):
            if mp[cur['#']] > 1:
                return
            if path:
                res.append(path[:])
            for c,node in cur.items():
                if c == '#':
                    continue
                path.append(c)
                dfs2(node, path)
                path.pop()
        dfs2(T, [])
        return res