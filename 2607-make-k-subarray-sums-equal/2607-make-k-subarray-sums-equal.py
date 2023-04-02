class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        for i in range(k):
            a = []
            j = i
            while arr[j%n] != 0:
                a.append(arr[j%n])
                arr[j%n] = 0
                j += k
            a.sort()
            if len(a) == 0:
                continue
            if len(a)%2:
                m = a[len(a)//2]
            else:
                m = (a[len(a)//2-1] + a[len(a)//2])//2
            for c in a:
                res += abs(c-m)
        return res
            