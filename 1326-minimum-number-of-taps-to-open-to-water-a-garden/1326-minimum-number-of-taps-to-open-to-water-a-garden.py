class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        A = [0]*(n+1)
        for i in range(n+1):
            A[i] = [i-ranges[i],i+ranges[i]]
        A.sort()
        l = 0
        r = 0
        res = 0
        # print(A)
        for a,b in A:
            if a <= l:
                r = max(r,b)
                if r >= n:
                    return res+1
            else:
                # print(l,r)
                res += 1
                if a > r:
                    return -1
                l = r
                r = max(r,b)
                # if r >= n:
                #     return res
        # print(l,r)
        # if r > l:
        #     res += 1
        return res if r >= n else -1