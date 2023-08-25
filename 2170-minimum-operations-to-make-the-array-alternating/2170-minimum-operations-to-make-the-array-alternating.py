class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        A = [[] for _ in range(2)]
        for i,n in enumerate(nums):
            A[i%2].append(n)
        E = sorted(list(Counter(A[0]).items()), key=lambda x:x[1])
        O = sorted(list(Counter(A[1]).items()), key=lambda x:x[1])
        if E[-1][0] != O[-1][0]:
            return len(A[0]) - E[-1][1] + len(A[1]) - O[-1][1]
        return min(len(A[0]) - (E[-2][1] if len(E) >= 2 else 0) + len(A[1]) - O[-1][1], len(A[0]) - E[-1][1] + len(A[1]) - (O[-2][1] if len(O) >= 2 else 0))
        