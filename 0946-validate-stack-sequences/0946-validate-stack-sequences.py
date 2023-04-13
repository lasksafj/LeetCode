class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = False
        st = [pushed[0]]
        i = 1
        j = 0
        while j < len(popped):
            while i < len(pushed) and (st == [] or popped[j] != st[-1]):
                st.append(pushed[i])
                i += 1
            if i == len(pushed) and popped[j] != st[-1]:
                return False
            st.pop()
            j += 1
        return True