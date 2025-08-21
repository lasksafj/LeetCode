class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        A = [0]*len(mat[0]) + [-inf]
        for row in mat:
            for i in range(len(A)-1):
                A[i] = (A[i] + row[i]) if row[i] > 0 else 0
            st = []
            for i in range(len(A)):
                while st and A[st[-1]] > A[i]:
                    mi = st.pop()
                    j = st[-1] if st else -1
                    if A[mi] > 0:
                        res += (i-mi) * (mi-j) * A[mi]                
                st.append(i)
        return res