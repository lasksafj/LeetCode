class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        a = [0]*n
        res = []
        prev = 0
        for i,c in queries:
            if a[i] != c:
                if i > 0 and a[i-1] == c and a[i-1] != a[i] and a[i-1] != 0:
                    prev += 1
                if i < n-1 and a[i+1] == c and a[i+1] != a[i] and a[i+1] != 0:
                    prev += 1
                if i > 0 and a[i-1] != c and a[i-1] == a[i] and a[i-1] != 0:
                    prev -= 1
                if i < n-1 and a[i+1] != c and a[i+1] == a[i] and a[i+1] != 0:
                    prev -= 1
            res.append(prev)
            a[i] = c
        return res