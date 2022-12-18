class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                a = st.pop()
                res[a] = i-a
            st.append(i)
        return res