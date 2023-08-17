class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i,j,prev_i = 0,N-1,0
        while i <= j:
            if nums[i] == 0:
                nums[i],nums[prev_i] = nums[prev_i],nums[i]
                if i == prev_i:
                    i += 1
                prev_i += 1
            elif nums[i] == 2:
                while j >= i and nums[j] == 2:
                    j -= 1
                if j > i:
                    nums[i],nums[j] = nums[j],nums[i]
            
            while i < N and nums[i] == 1:
                i += 1