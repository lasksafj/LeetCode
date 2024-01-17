class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        N = len(cars)
        res = [-1]*N
        st = []
        for i in range(N-1,-1,-1):
            p,v = cars[i]
            while st and (v <= cars[st[-1]][1] or (res[st[-1]] > 0 and (cars[st[-1]][0]-p) / (v-cars[st[-1]][1]) >= res[st[-1]])):
                st.pop()
            if st:
                res[i] = (cars[st[-1]][0]-p) / (v-cars[st[-1]][1])
            st.append(i)
        return res