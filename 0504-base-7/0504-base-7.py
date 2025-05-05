class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        a = abs(num)
        res = ''
        while a > 0:
            res += str(a%7)
            a //= 7
        return ('-' if num < 0 else '') + res[::-1]