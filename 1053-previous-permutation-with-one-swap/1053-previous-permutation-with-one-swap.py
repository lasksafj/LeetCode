class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        st = []
        for i in range(len(arr)-1,-1,-1):
            if st and arr[st[-1]] < arr[i]:
                ma = -1
                while st and arr[st[-1]] < arr[i]:
                    if ma == -1 or arr[ma] < arr[st[-1]]:
                        ma = st[-1]
                    st.pop()
                arr[ma],arr[i] = arr[i],arr[ma]
                return arr
            st.append(i)
        return arr