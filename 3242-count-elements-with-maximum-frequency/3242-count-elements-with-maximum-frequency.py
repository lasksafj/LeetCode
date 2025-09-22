class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ma = max(mp.values())
        return sum([b for a,b in mp.items() if b == ma])