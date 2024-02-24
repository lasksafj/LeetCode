prime = [1]*(1000000)
prime[0] = prime[1] = 0
for i in range(2,int(sqrt(1000000))):
    if prime[i]:
        for j in range(i*i, 1000000, i):
            prime[j] = 0

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        M,N = len(mat),len(mat[0])
        cnt = Counter()
        for i in range(M):
            for j in range(N):
                for di,dj in [[1,1],[-1,-1],[1,-1],[-1,1],[1,0],[0,1],[-1,0],[0,-1]]:
                    n = mat[i][j]
                    ni,nj = i+di,j+dj
                    while 0<=ni<M and 0<=nj<N:
                        n = n*10 + mat[ni][nj]
                        if prime[n]:
                            cnt[n] += 1
                        ni += di
                        nj += dj
        res = -1
        ma = 1
        for i in sorted(cnt.keys()):
            if cnt[i] >= ma:
                res = i
                ma = cnt[i]
        return res