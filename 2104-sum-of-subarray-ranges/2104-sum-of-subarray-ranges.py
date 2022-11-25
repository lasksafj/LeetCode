class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        st = []
        res1 = 0
        A = nums + [-inf]
        for i in range(len(A)):
            while st and A[st[-1]] > A[i]:
                a = st.pop()
                if st:
                    res1 += A[a] * (i-a) * (a-st[-1])
                else:
                    res1 += A[a] * (i-a) * (a+1)
            st.append(i)
            
        st = []
        res2 = 0
        A = nums + [inf]
        for i in range(len(A)):
            while st and A[st[-1]] < A[i]:
                a = st.pop()
                if st:
                    res2 += A[a] * (i-a) * (a-st[-1])
                else:
                    res2 += A[a] * (i-a) * (a+1)
            st.append(i)
        return res2 - res1