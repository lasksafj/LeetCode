class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        M,N = len(mat),len(mat[0])
        mask = 0
        for i in range(M):
            for j in range(N):
                mask |= mat[i][j]<<(i*N+j)
        
        q = deque([mask])
        vis = set()
        vis.add(mask)
        res = 0
        while q:
            # for n in q:
            #     print(bin(n),end=' ')
            # print()
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return res
                for i in range(M):
                    for j in range(N):
                        ncur = cur^(1<<(i*N+j))
                        for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                            if 0<=ni<M and 0<=nj<N:
                                ncur ^= (1<<(ni*N+nj))
                        if ncur not in vis:
                            vis.add(ncur)
                            q.append(ncur)
            res += 1
        return -1