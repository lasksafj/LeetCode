class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        res = 0
        arr.append(0)
        for i in range(len(arr)):
            while st and arr[st[-1]] > arr[i]:
                a = st.pop()
                if st:
                    res = (res + arr[a] * (i-a) * (a-st[-1])) % 1000000007
                else:
                    res = (res + arr[a] * (i-a) * (a+1)) % 1000000007
            st.append(i)
        return res % 1000000007