class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = ''
        if (numerator < 0) ^ (denominator < 0):
            res += '-'
        a,b = abs(numerator), abs(denominator)
        res += str(a//b)
        if a%b == 0:
            return res
        mp = {}
        frac = ''
        m = a%b
        i = 0
        while m:
            if m in mp:
                frac = frac[:mp[m]] + '(' + frac[mp[m]:] + ')'
                break
            mp[m] = i
            m *= 10
            frac += str(m//b)
            m %= b
            i += 1
        return res + '.' + frac