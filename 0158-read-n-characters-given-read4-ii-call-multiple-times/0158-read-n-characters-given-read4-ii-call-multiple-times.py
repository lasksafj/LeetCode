# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = ['']*4
        self.l4 = 0
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.l4 == 0:
                self.l4 = read4(self.buf4)
                if self.l4 == 0:
                    return i
            d = min(n-i, self.l4)
            buf[i:i+d] = self.buf4[:d]
            self.l4 = max(0, self.l4-d)
            for j in range(self.l4):
                self.buf4[j] = self.buf4[d+j]
            i += d
            
        return i