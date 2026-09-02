class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        M,N = len(classroom),len(classroom[0]) 
        nodes = []
        mp = defaultdict(int)
        noL = 0
        for i in range(M):
            for j in range(N):
                if classroom[i][j] == 'S':
                    si,sj = i,j
                elif classroom[i][j] == 'L':
                    mp[i,j] = 1<<noL
                    noL += 1
        q = deque()
        q.append([si,sj,0,energy])
        bestE = defaultdict(lambda:-1)
        bestE[si,sj,0] = energy
        step = 0
        while q:
            for _ in range(len(q)):
                i,j,mask,e = q.popleft()
                if mask == (1<<noL) - 1:
                    return step
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and classroom[ni][nj] != 'X' and e:
                        nmask = mask | mp[ni,nj]
                        ne = e-1 if classroom[ni][nj] != 'R' else energy
                        if bestE[ni,nj,nmask] < ne:
                            bestE[ni,nj,nmask] = ne
                            q.append([ni,nj,nmask,ne])
            step += 1
        return -1