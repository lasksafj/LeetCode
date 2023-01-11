class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        # def factorial(n) :
        #     fact = 1;
        #     for i in range(2, n + 1) :
        #         fact = (fact * i) % MOD
        #     return fact % MOD
        res = 1
        for w in s.split():
            b = 1
            for c,freq in Counter(w).items():
                b = (b * factorial(freq))
            res = (res * factorial(len(w)) // b) % MOD
        return res % MOD