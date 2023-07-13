class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        st = []
        nums.append(0)
        for i in range(len(nums)):
            cur = nums[i]
            while st and nums[st[-1]] >= cur:
                j = st.pop()
                l = st[-1]+1 if st else 0
                r = i if nums[j] == cur else i-1
                # if r-l+1 == 745:
                #     print(l,j,r,'--',nums[j])
                if nums[j] > threshold/(r-l+1):
                    return r-l+1
            st.append(i)
            
        return -1