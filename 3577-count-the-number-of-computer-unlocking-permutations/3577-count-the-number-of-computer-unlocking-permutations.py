class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] > min(complexity) or complexity[0] == min(complexity[1:]):
            return 0
        res = 1
        MOD = 10**9+7
        for i in range(len(complexity)-1, 0, -1):
            res = res*i % MOD
        return res