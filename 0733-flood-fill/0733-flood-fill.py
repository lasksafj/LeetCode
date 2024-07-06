class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = set()
        M,N = len(image),len(image[0])
        def dfs(i,j):
            vis.add((i,j))
            for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<M and 0<=nj<N and (ni,nj) not in vis and image[ni][nj] == image[i][j]:
                    dfs(ni,nj)
            image[i][j] = color
        dfs(sr,sc)
        return image