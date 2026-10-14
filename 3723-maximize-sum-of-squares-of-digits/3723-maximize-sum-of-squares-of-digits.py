class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num*9:
            return ''
        res = '9' * (sum//9)
        if sum%9:
            res += str(sum%9)
        res += '0' * (num - len(res))
        return res