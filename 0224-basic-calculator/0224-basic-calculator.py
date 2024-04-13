class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'
        postfix = []
        st = []
        i = 0
        prev_operator = ''
        while i < len(s):
            ch = s[i]
            if ch == ' ':
                i += 1
                continue
            if ch.isdigit():
                prev_operator = ''
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                postfix.append(int(s[i:j]))
                i = j-1
            elif ch == '(':
                prev_operator = '('
                st.append(ch)
            else:
                if st and st[-1] != '(':
                    b = postfix.pop()
                    a = postfix.pop()
                    if st.pop() == '+':
                        postfix.append(a+b)
                    else:
                        postfix.append(a-b)
                if ch == ')':
                    st.pop()
                else:
                    if prev_operator == '(':
                        postfix.append(0)
                    st.append(ch)
                prev_operator = ''
            i += 1
        return postfix[0]