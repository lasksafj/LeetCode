class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        st = deque()
        d = {'(':')', '{':'}','[':']'}
        for c in s:
            if c in d.keys():
                st.append(c);
            else:
                if len(st) == 0 or d[st.pop()] != c:
                    return False
        return len(st) == 0