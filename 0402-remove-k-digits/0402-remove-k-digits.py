class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num += '0'
        st = []
        for n in num:
            while st and st[-1] > n and k > 0:
                st.pop()
                k -= 1
            st.append(n)
        i = 0
        while i < len(st) and st[i] == '0':
            i += 1
        if i < len(st)-1:
            return ''.join(st[i:-1])
        return '0'