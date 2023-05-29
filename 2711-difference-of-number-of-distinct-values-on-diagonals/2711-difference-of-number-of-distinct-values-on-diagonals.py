class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        res = [[0]*n for _ in range(m)]
        suf = defaultdict(Counter)
        s = defaultdict(set)
        for i in range(m):
            for j in range(n):
                suf[i-j][grid[i][j]] += 1
        for i in range(m):
            for j in range(n):
                suf[i-j][grid[i][j]] -= 1
                if suf[i-j][grid[i][j]] == 0:
                    suf[i-j].pop(grid[i][j])
                res[i][j] = abs(len(s[i-j]) - len(suf[i-j]))
                s[i-j].add(grid[i][j])
        return res
        
            