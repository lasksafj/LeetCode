class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num*9:
            return ''
        res = ''
        for i in range(num):
            a = min(sum,9)
            res += str(a)
            sum -= min(sum,9)
        return res