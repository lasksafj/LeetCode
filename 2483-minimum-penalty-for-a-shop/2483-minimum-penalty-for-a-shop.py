class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = customers.count('Y')
        n = 0
        res = [0,y+n]
        for i,c in enumerate(customers):
            res = min(res, [i, y+n], key=lambda x: x[1])
            y -= c == 'Y'
            n += c == 'N'
        return min(res, [i+1, y+n], key=lambda x: x[1])[0]