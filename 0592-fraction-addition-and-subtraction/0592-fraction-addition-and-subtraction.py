class Solution:
    def fractionAddition(self, expression: str) -> str:
        def calc(s1,s2):
            s1 = [int(n) for n in s1.split('/')]
            s2 = [int(n) for n in s2.split('/')]
            nume = s1[0]*s2[1] + s2[0]*s1[1]
            deno = s1[1]*s2[1]
            d = gcd(nume, deno)
            return str(nume//d) + '/' + str(deno//d)
        
        A = []
        if expression[0] != '-':
            expression = '+' + expression
        i = 0
        while i < len(expression):
            j = i+1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            j += 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            A.append(expression[i:j])
            if len(A) == 2:
                A = [calc(A[0], A[1])]
            i = j
        if A[0][0] == '+':
            return A[0][1:]
        return A[0]