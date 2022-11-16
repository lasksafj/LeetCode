class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        res = []
        for a,b in Counter(nums).items():
            if b > n:
                res.append(a)
        return res