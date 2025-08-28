class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        i,j = m-1,0
        rev = 0
        for _ in range(m+n-1):
            a,b = i,j
            A = []
            while 0<=a<m and 0<=b<n:
                A.append(grid[a][b])
                a += 1
                b += 1
            A.sort(reverse=rev)
            a,b = i,j
            while 0<=a<m and 0<=b<n:
                grid[a][b] = A.pop()
                a += 1
                b += 1
            i -= 1
            if i < 0:
                j += 1
                i = 0
                rev = 1
        return grid