class Solution:
    def countElements(self, nums: List[int]) -> int:
        a,b = min(nums),max(nums)
        return len(nums) - nums.count(b) - nums.count(a) if a != b else 0