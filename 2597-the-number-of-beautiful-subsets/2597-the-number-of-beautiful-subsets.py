class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = defaultdict(int)
        
        def dfs(i):
            if i == len(nums):
                return 1
            pick = 0
            if nums[i]-k < 0 or m[nums[i]-k] == 0:
                m[nums[i]] += 1
                pick = dfs(i+1)
                m[nums[i]] -= 1
            notpick = dfs(i+1)
            return pick + notpick
        
        return dfs(0)-1