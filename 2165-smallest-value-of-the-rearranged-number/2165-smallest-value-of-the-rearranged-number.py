class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        A = sorted(str(num))
        if num < 0:
            return -int(''.join(A[1:][::-1]))
        i = 0
        while A[i] == '0':
            i += 1
        A = [A[i]] + ['0']*i + A[i+1:]
        return int(''.join(A))