class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix[0])
        A = [0]*N
        res = 0
        for row in matrix:
            A = [(a+int(r) if int(r) else 0) for a,r in zip(A,row)] + [-inf]
            st = []
            for i in range(N+1):
                while st and A[st[-1]] > A[i]:
                    j = st.pop()
                    l = st[-1] if st else -1
                    res = max(res, (i-l-1)*A[j])
                st.append(i)
        return res