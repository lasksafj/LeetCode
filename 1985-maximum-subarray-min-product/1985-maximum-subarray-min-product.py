class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(0)
        N = len(nums)
        res = 0
        pre = list(accumulate(nums, initial=0))
        st = []
        for i in range(N):
            while st and nums[st[-1]] >= nums[i]:
                j = st.pop()
                l = st[-1] if st else -1
                res = max(res, nums[j] * (pre[i]-pre[l+1]))
            st.append(i)
        return res % (10**9+7)