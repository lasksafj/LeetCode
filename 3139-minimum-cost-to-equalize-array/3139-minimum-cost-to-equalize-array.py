class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        # case 1: cost1 < cost2/2 -> use only op1
        # case 2: use 2 as many as possible, then use op1
        # case 3: add x to max(nums) to reduce op1, increase op2 (in case cost 1 >> cost 2)
        #   op1 = ma*(2-N) - 2*mi + sum(nums)
        #   ma->ma+1 => op1->op1+2-N = op1-(N-2)
        #   add until op1 < N-2 b/c op1 >= 0
        # case 4: add x to max(nums) until dont need to use op1 (cost 1 >>>> cost 2)
        
        ma, mi = max(nums), min(nums)
        N = len(nums)
        MOD = 10 ** 9 + 7
        needed = ma * N - sum(nums)
        # case 1
        if cost1*2 <= cost2 or N <= 2:
            return (needed * cost1) % MOD
        
        # case 2
        op1 = max(0, (ma-mi)*2 - needed)
        op2 = needed - op1
        res = (op1 + op2%2) * cost1 + op2//2 * cost2

        # case 3
        needed += op1//(N-2) * N
        op1 %= (N-2)
        op2 = needed - op1
        res = min(res, (op1 + op2%2) * cost1 + op2//2 * cost2 )
        
        # case 4
        for i in range(2):
            needed += N
            res = min(res, needed%2 * cost1 + needed//2 * cost2)
        return res % MOD