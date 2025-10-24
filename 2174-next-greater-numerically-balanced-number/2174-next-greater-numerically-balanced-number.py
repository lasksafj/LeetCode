A = []
B = []
for mask in range(1, 1<<7+1):
    s = 0
    A = []
    for i in range(len(bin(mask)[2:])):
        if mask&(1<<i):
            s += i+1
            A += [i+1]*(i+1)
    if len(A) > 7: continue
    for a in permutations(A):
        d = int(''.join(str(c) for c in a))
        B.append(d)
B.sort()

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return B[bisect_right(B, n)]