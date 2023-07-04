class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for n in asteroids:
            if n > 0 or (st and st[-1]*n > 0):
                st.append(n)
            else:
                while st and 0 < st[-1] <= -n:
                    a = st[-1]
                    st.pop()
                    if a == -n:
                        n = 0
                        break
                if n != 0 and (st == [] or st[-1] < 0):
                    st.append(n)
            # print(st)
        return st
                