class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)
        if log10(int(n)).is_integer() or log10(int(n)-1).is_integer():
            return '9' * (len(n)-1)
        if log10(int(n)+1).is_integer():
            return '1' + '0'*(len(n)-1) + '1'
        l = len(n)-1
        p = l//2
        if l%2:
            a = n[:p+1] + n[:p+1][::-1]
            b = str(int(n[:p+1]) + 1)
            b = b[:p+1] + b[:p+1][::-1]
            c = str(int(n[:p+1]) - 1)
            c = c[:p+1] + c[:p+1][::-1]
        else:
            a = n[:p+1] + n[:p][::-1]
            b = str(int(n[:p+1]) + 1)
            b = b[:p+1] + b[:p][::-1]
            c = str(int(n[:p+1]) - 1)
            c = c[:p+1] + c[:p][::-1]
        
        a,b,c,n = int(a),int(b),int(c),int(n)
        if a == n:
            res = min(c,b, key=lambda x: abs(n-x))
        else:
            res = min(c,a,b, key=lambda x: abs(n-x))
        return str(res)