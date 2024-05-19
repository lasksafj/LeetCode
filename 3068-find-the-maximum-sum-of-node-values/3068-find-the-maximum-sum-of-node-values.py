class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dpa,dpb = 0,-inf
        for n in nums:
            n_dpa = max(dpa+n, dpb+(n^k))
            n_dpb = max(dpb+n, dpa+(n^k))
            dpa,dpb = n_dpa,n_dpb
        return dpa