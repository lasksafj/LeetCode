class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        res = 0
        n = money//8
        # print('n',n)
        # print('children',children)
        if children*8 == money:
            res = children
        elif children <= n:
            res = children-1
        elif children == n+1:
            res = n if money%8 != 4 and money%8!=0 else n-1
        else:
            if children-n-money%8 > 0:
                res = n - ceil((children-n-money%8)/7)
            elif children-n-money%8 <= 0:
                res = n
        return res