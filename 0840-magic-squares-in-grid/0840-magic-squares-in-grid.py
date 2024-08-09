class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        def check(si,sj):
            if M-si<3 or N-sj<3:
                return False
            sr,sc = [0]*3,[0]*3
            sd1,sd2 = 0,0
            vis = set()
            for i in range(si,si+3):
                for j in range(sj,sj+3):
                    n = grid[i][j]
                    if n<1 or n>9 or n in vis:
                        return False
                    vis.add(n)
                    r,c = i-si,j-sj
                    sr[r] += n
                    sc[c] += n
                    if r==c:
                        sd1 += n
                    if r==2-c:
                        sd2 += n
            return sr[0]==sr[1] and sr[1]==sr[2] and sc[0]==sc[1] and sc[1]==sc[2] and sr[0]==sd1 and sd1==sd2
        res = 0
        for i in range(M):
            for j in range(N):
                res += check(i,j)
        return res