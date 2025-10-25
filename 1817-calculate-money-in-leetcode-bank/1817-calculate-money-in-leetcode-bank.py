class Solution:
    def totalMoney(self, n: int) -> int:
        b = (1+7)*7//2
        a = n//7
        weeks = a*b + 7 * (a-1)*a//2
        c = n%7
        last_week = c*(c+1)//2 + a*c
        return weeks + last_week