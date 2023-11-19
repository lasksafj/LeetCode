class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        A = sorted(mp.keys())[::-1]
        res = 0
        for i in range(len(A)-1):
            res += mp[A[i]]
            mp[A[i+1]] += mp[A[i]]
        return res