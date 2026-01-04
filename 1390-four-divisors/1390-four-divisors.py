N = 10**5+1
prime = [1]*N
prime[0] = prime[1] = 0
for i in range(2, N):
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = 0
prime_arr = [i for i in range(N) if prime[i]]
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if prime[n]: continue
            for p in prime_arr:
                if p*p >= n: break
                if n%p != 0: continue
                if prime[n//p] or n//p == p*p:
                    res += 1 + n + p + n//p
                    break
        return res