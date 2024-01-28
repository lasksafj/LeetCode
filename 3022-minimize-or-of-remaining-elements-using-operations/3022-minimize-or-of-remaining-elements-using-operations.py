class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        # check whether can clear bits in mask using at most k operations
        def can_off(mask):
            A = [n&mask for n in nums]
            i = 0
            res = 0
            while i < len(A):
                if A[i] == 0:
                    i += 1
                    continue
                j = i+1
                cur = A[i]
                while j < len(A) and cur & A[j]:
                    cur &= A[j]
                    j += 1
                res += j-i
                i = j+1
            return res <= k
        
        mask = 0
        for i in range(29,-1,-1):
            if can_off(mask|(1<<i)):
                mask |= (1<<i)
        return (1<<30)-1 - mask