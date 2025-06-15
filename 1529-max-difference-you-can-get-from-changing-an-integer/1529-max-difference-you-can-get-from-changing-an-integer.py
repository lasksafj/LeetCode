class Solution:
    def maxDiff(self, num: int) -> int:
        ma,mi = str(num), str(num)
        for d in ma:
            if d < '9':
                ma = ma.replace(d, '9')
                break
        for i,d in enumerate(mi):
            if i == 0 and d > '1':
                mi = mi.replace(d, '1')
                break
            if d > '0' and d != mi[0]:
                mi = mi.replace(d, '0')
                break
        return int(ma) - int(mi)