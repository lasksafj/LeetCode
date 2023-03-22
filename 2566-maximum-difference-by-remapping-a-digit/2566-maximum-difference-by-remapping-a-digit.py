class Solution:
    def minMaxDifference(self, num: int) -> int:
        a = []
        while num > 0:
            a.append(num%10)
            num //= 10
        i = len(a)-1
        while i >= 0 and a[i] == 9:
            i -= 1
        mi,ma = {},{}
        if i >= 0:
            ma[a[i]] = 9
        mi[a[-1]] = 0
        x,y = 0,0
        for n in a[::-1]:
            if n in ma:
                x = x*10 + ma[n]
            else:
                x = x*10 + n
            if n in mi:
                y = y*10 + mi[n]
            else:
                y = y*10 + n
        return x-y