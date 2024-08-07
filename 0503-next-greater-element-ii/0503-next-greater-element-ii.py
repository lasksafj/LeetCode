class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        A = nums+nums
        res = [-1]*N
        st = []
        for i in range(len(A)):
            while st and A[st[-1]] < A[i]:
                j = st.pop()
                if j < N and res[j] == -1:
                    res[j] = i%N
            st.append(i)
        return [nums[i] if i>-1 else -1 for i in res]