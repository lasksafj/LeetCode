class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        res = []
        for i,n in enumerate(nums):
            while st and nums[st[-1]] < n:
                st.pop()
            st.append(i)
            if i-st[0] >= k:
                st.popleft()
            if i >= k-1:
                res.append(nums[st[0]])
        return res