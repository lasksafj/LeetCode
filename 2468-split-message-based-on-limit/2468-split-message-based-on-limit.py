class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def check(x, mess_len, limit):
            nlen = 0
            if x < 10:
                nlen = 5*x + mess_len
            elif x < 100:
                nlen = 6*9 + 7*(x-9) + mess_len
            elif x < 1000:
                nlen = 7*9 + 8*90 + 9*(x-99) + mess_len
            else:
                nlen = 8*9 + 9*90 + 10*900 + 11*(x-999) + mess_len
            if nlen % limit == 0:
                return nlen//limit
            return nlen//limit + 1
        
        
        mess_len = len(message)
        # print(check(19, mess_len, limit))
        l,r = 0,mess_len+1
        while l < r:
            m = (l+r)//2
            # print(m, check(m, mess_len, limit))
            if check(m, mess_len, limit) < m:
                r = m-1
            elif check(m, mess_len, limit) > m:
                l = m+1
            else:
                r = m
                # break
        if l == 0 or l == mess_len+1:
            return []
        
        res = []
        no_part = l
        part = 0
        i = 0
        while i < mess_len:
            a = []
            part += 1
            suffix = '<' + str(part) + '/' + str(no_part) + '>'
            j = 0
            while i < mess_len and j < limit - len(suffix):
                a.append(message[i])
                i += 1
                j += 1
            a.append(suffix)
            res.append(''.join(a))
        return res
                