class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = []
        b = []
        for i in range(1, int(sqrt(n))+1):
            if n%i == 0:
                a.append(i)
                if i != n//i:
                    b.append(n//i)
        if k > len(a) + len(b):
            return -1
        if k <= len(a):
            return a[k-1]
        return b[-(k-len(a))]
