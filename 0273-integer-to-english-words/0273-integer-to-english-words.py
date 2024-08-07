class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        tbm = ('Thousand', 'Million', 'Billion')
        
        def dfs(n):
            if n == 0:
                return ''
            if n < 20:
                return ' ' + to19[n]
            if n < 100:
                return ' ' + tens[n//10] + dfs(n%10)
            if n < 1000:
                return dfs(n//100) + ' Hundred' + dfs(n%100)
            for i in range(3):
                if n < 1000**(i+2):
                    return dfs(n//(1000**(i+1))) + ' ' + tbm[i] + dfs(n%(1000**(i+1)))
            return ''
        return dfs(num).strip()