class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        m = 1
        s = set()
        i = 1
        while m and m not in s:
            s.add(m)
            m = (m*10 + 1)%k
            i += 1
        return i if m == 0 else -1