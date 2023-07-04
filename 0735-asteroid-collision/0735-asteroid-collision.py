class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for n in asteroids:
            while st and st[-1] > 0 and n < 0:
                if st[-1] + n < 0:
                    st.pop()
                elif st[-1] + n > 0:
                    n = 0
                    break
                else:
                    st.pop()
                    n = 0
                    break
            if n != 0:
                st.append(n)
        return st
                