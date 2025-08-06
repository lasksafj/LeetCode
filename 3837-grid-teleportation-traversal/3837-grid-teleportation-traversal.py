class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        M,N = len(matrix),len(matrix[0])
        mp = defaultdict(list)
        for i in range(M):
            for j in range(N):
                mp[matrix[i][j]].append((i,j))
        q = deque([[0,0]])
        vis = {(0,0)}
        if matrix[0][0] != '.':
            q = deque(mp[matrix[0][0]])
            vis = set(mp[matrix[0][0]])
        res = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if (i,j) == (M-1,N-1):
                    return res
                for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=ni<M and 0<=nj<N and matrix[ni][nj] != '#' and (ni,nj) not in vis:
                        A = [[ni,nj]]
                        if matrix[ni][nj] != '.':
                            A = mp[matrix[ni][nj]]
                        for nni,nnj in A:
                            q.append([nni,nnj])
                            vis.add((nni,nnj))
            res += 1
        return -1