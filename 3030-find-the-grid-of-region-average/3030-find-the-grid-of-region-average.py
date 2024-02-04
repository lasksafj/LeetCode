class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        M,N = len(image),len(image[0])
        res = [[[] for _ in range(N)] for _ in range(M)]
        
        for i in range(M-2):
            for j in range(N-2):
                s = 0
                is_region = True
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        s += image[ii][jj]
                        if ii < i+2 and abs(image[ii][jj]-image[ii+1][jj]) > threshold \
                        or jj < j+2 and abs(image[ii][jj]-image[ii][jj+1]) > threshold:
                            is_region = False
                if is_region:
                    for ii in range(i,i+3):
                        for jj in range(j,j+3):
                            res[ii][jj].append(s//9)
        for i in range(M):
            for j in range(N):
                if res[i][j]:
                    res[i][j] = sum(res[i][j])//(len(res[i][j]))
                else:
                    res[i][j] = image[i][j]
        
        return res