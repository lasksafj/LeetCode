def check(grid,x,y,tx,ty,bx,by):
    M,N = len(grid),len(grid[0])
    if tx<0 or tx==M or ty<0 or ty==N or grid[tx][ty] == '#':
        return False
    A = [e.copy() for e in grid]
    for i in range(M):
        for j in range(N):
            if A[i][j] == 'B' or A[i][j] == 'T' or A[i][j] == 'S':
                A[i][j] = '.'
    A[bx][by] = 'B'
    
    q = deque([(x,y)])
    vis = set()
    vis.add((x,y))
    while q:
        i,j = q.popleft()
        if i==tx and j==ty:
            return True
        for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if 0<=ni<M and 0<=nj<N and A[ni][nj] == '.' and (ni,nj) not in vis:
                vis.add((ni,nj))
                q.append((ni,nj))
    # print(x,y,tx,ty,bx,by)
    # for e in A:
    #     print(e)
    return False

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        bi,bj,si,sj,ti,tj = 0,0,0,0,0,0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 'B':
                    bi,bj = i,j
                elif grid[i][j] == 'S':
                    si,sj = i,j
                elif grid[i][j] == 'T':
                    ti,tj = i,j
        
        i,j = bi,bj
        q = deque()
        vis = set()
        q.append([bi,bj,si,sj])
        vis.add((bi,bj,si,sj))
        # for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        #     if 0<=ni<M and 0<=nj<N and grid[ni][nj] != '#':
        #         if check(grid,si,sj,ni,nj,bi,bj):
        #             q.append([i,j,ni,nj])
        #             vis.add((i,j,ni,nj))
        
        
        res = 0
        while q:
            # print(q)
            for _ in range(len(q)):
                i,j,si,sj = q.popleft()
                if i==ti and j==tj:
                    return res
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and grid[ni][nj] != '#' and (ni,nj,i,j) not in vis:
                        if check(grid,si,sj,i+i-ni,j+j-nj,i,j):
                            q.append([ni,nj,i,j])
                            vis.add((ni,nj,i,j))
            res += 1
        return -1
            
                                    