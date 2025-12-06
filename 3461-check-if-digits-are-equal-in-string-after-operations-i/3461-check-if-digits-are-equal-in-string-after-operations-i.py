def all_nCk_mod10(n):
    # 1) Precompute v2[i], v5[i], rem[i] = i // (2^v2 * 5^v5) mod 10,
    #    and inv_rem[i] = modular inverse of rem[i] mod 10 (possible since rem[i]∈{1,3,7,9}).
    v2 = [0]*(n+1)
    v5 = [0]*(n+1)
    rem = [1]*(n+1)
    inv_rem = [1]*(n+1)
    # inverses mod 10 of 1,3,7,9
    inv_map = {1:1, 3:7, 7:3, 9:9}
    for i in range(1, n+1):
        x = i
        while x % 2 == 0:
            v2[i] += 1
            x //= 2
        while x % 5 == 0:
            v5[i] += 1
            x //= 5
        rem[i] = x % 10
        inv_rem[i] = inv_map[rem[i]]
    
    # Precompute 2^e mod 10 cycle for e>=1
    two_cycle = [6, 2, 4, 8]  # 2^1=2,2^2=4,2^3=8,2^4=6,2^5=2,...

    result = [0]*(n+1)
    odd_part = 1   # product of rem’s so far mod10
    e2 = e5 = 0    # exponent counters

    # k=0: C(n,0)=1
    result[0] = 1

    for k in range(1, n+1):
        # multiply by (n−k+1)
        e2 += v2[n-k+1]
        e5 += v5[n-k+1]
        odd_part = (odd_part * rem[n-k+1]) % 10

        # divide by k
        e2 -= v2[k]
        e5 -= v5[k]
        odd_part = (odd_part * inv_rem[k]) % 10

        # reassemble mod 10
        if e2 > 0 and e5 > 0:
            result[k] = 0
        elif e5 > 0:            # odd * 5
            result[k] = 5
        elif e2 > 0:            # odd * 2^e2
            # if e2==0, we’d use 1, so handle separately
            p2 = two_cycle[e2 % 4] if e2 > 0 else 1
            result[k] = (odd_part * p2) % 10
        else:
            result[k] = odd_part  # fully odd

    return result



class Solution:
    def hasSameDigits(self, s: str) -> bool:
        A = [int(c) for c in s]
        B = all_nCk_mod10(len(A)-2)
        def f(A):
            res = 0
            for k,a in enumerate(A):
                res = (res + B[k] * a) % 10
            return res
        return f(A[:-1]) == f(A[1:])