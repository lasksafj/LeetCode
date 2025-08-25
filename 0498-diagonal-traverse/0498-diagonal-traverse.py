class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M,N = len(mat),len(mat[0])
        mp = [[] for _ in range(M+N-1)]
        for i in range(M):
            for j in range(N):
                mp[i+j].append(mat[i][j])
        res = []
        for i in range(len(mp)):
            if i&1:
                res += mp[i]
            else:
                res += mp[i][::-1]
        return res