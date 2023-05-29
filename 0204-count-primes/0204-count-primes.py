class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True]*n
        prime[0]=prime[1]=False
        for i in range(2,int(sqrt(n))+1):
            if prime[i]:
                prime[i*i:n:i] = [False] * len(prime[i*i:n:i])
        return sum(prime)