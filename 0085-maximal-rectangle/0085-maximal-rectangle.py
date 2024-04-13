class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M,N = len(matrix),len(matrix[0])
        row = [0]*(N+1)
        res = 0
        for i in range(M):
            st = []
            for j in range(N):
                row[j] = (row[j] + int(matrix[i][j])) if matrix[i][j] == '1' else 0
            for j in range(N+1):
                while st and row[st[-1]] > row[j]:
                    a = row[st.pop()]
                    l = st[-1] if st else -1
                    res = max(res, (j-l-1)*a )
                st.append(j)
        return res