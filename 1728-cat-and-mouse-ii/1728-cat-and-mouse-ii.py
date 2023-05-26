class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        @cache
        def dfs(mx,my,cx,cy,turn,mturn):
            if (mx==cx and my==cy) or grid[cx][cy] == 'F' or turn == 0:
                return False
            if grid[mx][my] == 'F':
                return True
            if mturn:
                res = False
                for d in [[1,0],[-1,0],[0,1],[0,-1]]:
                    for j in range(mouseJump+1):
                        nmx,nmy = mx+d[0]*j, my+d[1]*j
                        if nmx<0 or nmy<0 or nmx>=m or nmy>=n or grid[nmx][nmy]=='#':
                            break
                        a = dfs(nmx,nmy,cx,cy,turn-1,mturn^1)
                        if a == True:
                            return True
                return False
            else:
                res = True
                for d in [[1,0],[-1,0],[0,1],[0,-1]]:
                    for j in range(catJump+1):
                        ncx,ncy = cx+d[0]*j, cy+d[1]*j
                        if ncx<0 or ncy<0 or ncx>=m or ncy>=n or grid[ncx][ncy]=='#':
                            break
                        a = dfs(mx,my,ncx,ncy,turn,mturn^1)
                        if a == False:
                            return False
                return True
                
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'M':
                    mx = i
                    my = j
                elif grid[i][j] == 'C':
                    cx = i
                    cy = j
        return dfs(mx,my,cx,cy,m*n,1)