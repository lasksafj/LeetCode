class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # tree -> not cycle -> only 1 path between 2 nodes -> can replace any 2 nodes with their xor values
        # can replace any even number of nodes with their xor values
        dpa,dpb = 0,-inf
        for n in nums:
            n_dpa = max(dpa+n, dpb+(n^k))
            n_dpb = max(dpb+n, dpa+(n^k))
            dpa,dpb = n_dpa,n_dpb
        return dpa