class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # order s to 000..111...
        # result: M moves
        # bi: number of times we flip ith-bit
        # z: number of bit are zeros
        # b1, b2,..., bz: odd number (1)
        # bz+1,..., bN-z: even number (2)
        # bi <= M (3)

        # also we have M >= z/k (4)

        # initially, place b1=b2=...bz=1, remaining flips: E = Mk-z, we must add an even amount to each bi => E even => Mk same parity as z (5)
        # if M even, 
        #     (1,3) => b1,...,bz <= M-1
        #     (2,3) => bz+1,...,bN-z <= M
        #     => z(M-1) + (N-z)M <= Mk 
        #     -z-MN <= Mk 
        #     M >= z/(N-k) (6)
        # if M odd,
        #     (1,3) => b1,...,bz <= M
        #     (2,3) => bz+1,...,bN-z <= M-1
        #     => zM + (N-z)(M-1) <= Mk
        #     M >= (N-z)/(N-k) (7)

        # (4,5,6,7) => ans

        N = len(s)
        z = s.count('0')
        if N == k:
            if z == 0: return 0
            if z == N: return 1
            return -1
        res = inf
        # M even
        if z%2 == 0:
            M = max(ceil(z/k), ceil(z/(N-k)))
            if M&1:
                M += 1
            res = min(res, M)
        # M odd
        if z%2 == k%2:
            M = max(ceil(z/k), ceil((N-z)/(N-k)))
            if M&1 == 0:
                M += 1
            res = min(res, M)
        return res if res < inf else -1