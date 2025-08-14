class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = '-1'
        for i in range(len(num)-2):
            a = num[i:i+3]
            if len(set(a)) == 1:
                res = max(res, a, key=lambda x:int(x))
        return res if int(res) > -1 else ''