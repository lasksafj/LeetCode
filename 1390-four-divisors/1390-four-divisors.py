class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            sqrt_i = int(sqrt(i))
            no_divisor = 0
            cur = 0
            for j in range(1, sqrt_i+1):
                if i%j == 0:
                    no_divisor += 2
                    cur += j + i//j
            if sqrt_i**2 == i:
                no_divisor -= 1
                cur -= sqrt_i
            if no_divisor == 4:
                res += cur
        return res
            