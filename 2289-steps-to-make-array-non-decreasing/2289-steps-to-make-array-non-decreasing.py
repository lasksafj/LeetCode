class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0]*len(nums) #no numbers that nums[i] can eat on its right
        st = []
        for i in range(len(nums)-1,-1,-1):
            cur = 1
            while st and nums[st[-1]] < nums[i]:
                dp[i] = max(dp[i]+1, dp[st.pop()])
            st.append(i)
        return max(dp)