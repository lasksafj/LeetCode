class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = []
        for e in tokens:
            if e in '+-*/':
                b = dq.pop()
                a = dq.pop()
                if e == '+':
                    dq.append(a+b)
                elif e == '-':
                    dq.append(a-b)
                elif e == '*':
                    dq.append(a*b)
                else:
                    dq.append(int(a/b))
            else:
                dq.append(int(e))
        return dq[0]