n = 1000000
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False
A = []
for i in range(2, n):
    if is_prime[i]: 
        A.append(i)
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                d = int(s[i:j+1])
                if d <= n: 
                    if is_prime[d]:
                        primes.add(d)
                    continue
                b = int(sqrt(d))
                ok = 1
                for a in A:
                    if a > b:
                        break
                    if d%a == 0:
                        ok = 0
                        break
                if ok:
                    primes.add(d)
        return sum(sorted(list(primes))[-3:])