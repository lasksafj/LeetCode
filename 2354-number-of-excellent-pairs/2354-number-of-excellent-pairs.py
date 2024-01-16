class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        A = []
        nums = set(nums)
        N = len(nums)
        for n in nums:
            A.append(bin(n).count('1'))
        A.sort()
        res = 0
        for a in A:
            p = bisect_left(A, k-a)
            res += N-p
        return res