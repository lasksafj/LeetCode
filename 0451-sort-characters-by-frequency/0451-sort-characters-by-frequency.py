class Solution:
    def frequencySort(self, s: str) -> str:
        m = [[0,chr(i)] for i in range(128)]
        for c in s:
            i = ord(c)
            m[i][0] += 1
        m.sort(key=lambda x: -x[0])
        s = ''
        for e in m:
            if e[0] > 0:
                s += e[0]*e[1]
        return s