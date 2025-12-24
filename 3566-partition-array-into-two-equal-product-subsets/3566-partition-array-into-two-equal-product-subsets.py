class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        for mask in range(1<<N):
            d1 = 1
            d2 = 1
            for i in range(N):
                if (1<<i) & mask:
                    d1 *= nums[i]
                else:
                    d2 *= nums[i]
            if d1 == target and d2 == target:
                return True
        return False