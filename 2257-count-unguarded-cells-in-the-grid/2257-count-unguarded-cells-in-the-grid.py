class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        A = [[0]*n for _ in range(m)]
        for i,j in guards:
            A[i][j] = 1
        for i,j in walls:
            A[i][j] = -1
        # for e in A:
        #     print(e)
        for i in range(m):
            d = 0
            for j in range(n):
                if A[i][j] == 1:
                    d = 2
                elif A[i][j] == -1:
                    d = 0
                else:
                    A[i][j] = d
            d = 0
            for j in range(n-1,-1,-1):
                if A[i][j] == 1:
                    d = 2
                elif A[i][j] == -1:
                    d = 0
                elif A[i][j] != 2:
                    A[i][j] = d
        for j in range(n):
            d = 0
            for i in range(m):
                if A[i][j] == 1:
                    d = 2
                elif A[i][j] == -1:
                    d = 0
                elif A[i][j] != 2:
                    A[i][j] = d
            d = 0
            for i in range(m-1,-1,-1):
                if A[i][j] == 1:
                    d = 2
                elif A[i][j] == -1:
                    d = 0
                elif A[i][j] != 2:
                    A[i][j] = d
        res = 0
        # print('------------------')
        # for e in A:
        #     print(e)
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    res += 1
        return res