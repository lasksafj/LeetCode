class Solution:
    def canSeePersonsCount(self, H: List[int]) -> List[int]:
        st = []
        H = [inf] + H
        res = [0]*len(H)
        for i in range(len(H)-1,-1,-1):
            h = H[i]
            while st and H[st[-1]] < h:
                j = st.pop()
                res[i] += 1
            if st:
                res[i] += 1
            st.append(i)
        return res[1:]