class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        res = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res += m[s - goal]
            m[s] += 1
            
        return res