class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0]*len(nums) 
        st = []
        for i in range(len(nums)):
            cur = 0
            while st and nums[st[-1]] <= nums[i]:
                cur = max(cur, dp[st.pop()])
            if st:
                dp[i] = cur+1
            st.append(i)
        return max(dp)